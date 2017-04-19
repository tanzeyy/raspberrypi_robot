#!/usr/bin/env python

# Local modules
from arm import Arm
from classifier import Classifier
from move import Move
from search import get_route
from dicts import *


class Robot(Arm, Classifier, Move):
    def __init__(self):
        print("Initializing...")
        Arm.__init__(self)
        Classifier.__init__(self)
        Move.__init__(self)
        self.set_direction('right')
        self.move_by_block(1)
        self.waze = (1, 3)
        print("Initialize over")

    def get_waze(self):
        print(self.waze)
        return self.waze

    def classify(self, shelf, side):
        return self.get_classify_results(self, shelf, side)

    def move(self, dirc, arg, method='block', speed='fast'):
        self.set_direction(dirc)
        self.set_speed(speed)
        if method == 'block':
            self.move_by_block(arg)
        elif method == 'time':
            self.move_by_time(arg)
        else:
            raise Exception("Move method input error!")

    def run_to_goal(self, goal):
        route = get_route(self.waze, goal)
        for way in route:
            self.move(way[0], way[1])
        self.waze = goal

    def route_to_grid(self, grid, method='in'):
        (x1, y1) = self.waze
        (x2, y2) = grid
        if x1 < x2:
            first = 'right'
            if y1 < y2:
                second = 'up'
            elif y1 > y2:
                second = 'down'
            else:
                second = 'no'
        elif x1 > x2:
            first = 'left'
            if y1 < y2:
                second = 'up'
            elif y1 > y2:
                second = 'down'
            else:
                second = 'no'
        else:
            first = 'no'
            if y1 < y2:
                second = 'up'
            elif y1 > y2:
                second = 'down'
            else:
                second = 'no'

        route = filter(lambda dirc: dirc != 'no', [first, second])
        # Way to exit grid
        trans = {'up': 'down', 'right': 'left',
                 'down': 'up', 'left': 'right')
        if method == 'in':
            route = route
        elif method == 'exit':
            route = map(lambda dirc: trans[dirc], route)
        else:
            raise Exception("Grid method input error!")

        for dirc in route:
            self.move(dirc, 1, 'time')

    def grab_obj(self, obj_name, block):
        obj = get_obj(obj_name)
        obj_paw = obj.get_paw()

        shelf = block[0:1]
        other_shelf = filter(lambda x: x != shelf, ['A', 'B', 'C', 'D'])[0]
        pos = get_position(block)
        pre_act = pos[0]
        end_act = pos[1]

        # Actions of grab objects
        self.act(pre_act)
        self.grab(obj_paw)
        self.act(end_act)
        self.rotate_to_shelf(other_shelf)

    def place_obj(self, obj_name):
        obj = get_obj(obj_name)
        obj_cart = obj.get_cart()
        self.rotate_to_cart(obj_cart)
        self.place()


robot = Robot()


def grab_place():
