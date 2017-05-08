#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

# Local modules
from arm import Arm
from classifier import Classifier
from move import Move
from search import get_route
from dicts import *

from collections import OrderedDict
import time


class Robot(Arm, Classifier, Move):
    def __init__(self):
        # Initialize the properties of the meta class
        print("Initializing...")
        Arm.__init__(self)
        Classifier.__init__(self)
        Move.__init__(self)

        # Run to the start location
        self.set_direction('right')
        self.move_by_grid(1)
        self.__waze = (1, 3)
        print("Initialize over")

    def get_waze(self):
        # Return the current location
        return self.__waze

    def set_waze(self, coordinate):
        self.__waze = coordinate

    def classify(self, shelf, side):
        # Get the block: obj pair of what is detected
        return self.capture_and_classify(shelf, side)

    def move(self, dirc, arg, method='grid', speed='fast'):
        self.set_direction(dirc)
        self.set_speed(speed)

        if method == 'grid':
            moved_distance = self.move_by_grid(arg)
        elif method == 'time':
            moved_distance = self.move_by_time(arg)
        else:
            raise Exception("Move method input error!")

        return moved_distance

    def correct_movement_error(self, direction):
        corr_dirc = trans[direction]
        self.set_direction(corr_dirc)
        current_speed = self.speed
        self.set_speed('slow')
        time.sleep(0.2)
        self.move_by_time(2.5)
        self.set_speed(current_speed)

    def run_to_goal(self, goal):
        # Get the route of current location to the goal
        route, length = get_route(self.__waze, goal)
        print(route)

        for way in route:
            direction = way[0]
            total_distance = way[1]
            move_distance = total_distance - 1
            if total_distance > 1:
                while True:
                    move_distance = self.move(direction, move_distance,
                                              'grid', 'fast')
                    # Check for error
                    if move_distance != 0:
                        self.correct_movement_error(direction)
                    else:
                        break

            # Decelerate in the last grid and check for error
            while True:
                move_distance = self.move(direction, 1, 'grid', 'slow')
                if move_distance != 0:
                    self.correct_movement_error(direction)
                else:
                    break

        self.__waze = goal
        print("Current waze: ", self.__waze)

    def run_in_grid(self, grid, method='in'):
        # Determine the route of current location to the place-location
        (x1, y1) = self.__waze
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

        # Filter out the 'no' route
        route = filter(lambda dirc: dirc != 'no', [first, second])

        if method == 'in':
            route = route
        elif method == 'exit':
            # Convert the incoming path to exit path
            route = map(lambda dirc: trans[dirc], route)
        else:
            raise Exception("Grid method input error!")

        for dirc in route:
            self.move(dirc, 1.2, 'time', 'slow')

    def grab_obj(self, obj_name, block):
        # Get the information of the block
        shelf = block[0:1]
        back_block_goal = get_back_coordinates(block)
        # other_shelf = filter(lambda x: x != shelf, ['A', 'B', 'C', 'D'])[0]
        pos = get_position(obj_name, block)
        pre_act = pos[0]
        # end_act = pos[1]

        # Get the information of the object
        obj = get_obj(obj_name)
        obj_paw = obj.get_paw(block)

        # Actions of grab objects
        print("Start grab %s..." % obj_name)
        self.arm_port.flushOutput()
        self.rotate_to_shelf(shelf)
        self.act(pre_act)
        self.grab(obj_paw)
        # Go back first after grabbed object
        self.run_to_goal(back_block_goal)
        # self.act(end_act)
        # self.rotate_to_shelf(other_shelf)
        self.restore()
        print("Grab over!")

    def place_obj(self, obj_name):
        # Get the information of the cart to place the holding object
        obj = get_obj(obj_name)
        obj_cart = obj.get_cart()
        print("Start place %s..." % obj_name)
        self.arm_port.flushOutput()
        self.rotate_to_cart(obj_cart)
        self.place()
        self.restore()
        print("Place over!")


robot = Robot()


def grab_and_place(obj_name, block):

    # Get the coordinate of detected block
    block_goal = get_coordinates(block)

    # Obtain obj information from the Objs class
    obj = get_obj(obj_name)
    obj_goal = obj.get_goal()
    obj_cart = obj.get_cart()
    obj_grid = obj.get_grid()
    obj_pre_paw = obj.get_pre_paw()

    # Actions of grab and place an object
    robot.rotate_paw(obj_pre_paw)
    robot.run_to_goal(block_goal)
    robot.grab_obj(obj_name, block)

    # Go to place object
    robot.run_to_goal(obj_goal)
    robot.run_in_grid(obj_grid)
    robot.place_obj(obj_name)
    time.sleep(0.8)
    robot.run_in_grid(obj_grid, 'exit')
    time.sleep(0.3)


def get_shortest_route(results):
    # Initial the start point and shortest_route
    start_point = (2, 6)
    l = 100
    shortest_route = OrderedDict()

    while len(results) != 0:
        for block, obj_name in results.items():
            route, length = get_route(start_point, get_coordinates(block))
            if l >= length:
                l = length
                next_obj = obj_name
                next_block = block
        # Find the nearest block, store the objects in shortest_route
        start_point = get_obj(next_obj).get_goal()
        shortest_route[next_block] = next_obj
        results.pop(next_block)
        l = 100

    return shortest_route


def capture_images_of_one_shelf(shelf):
    shelf_goal = get_shelf_goal(shelf)
    num = 1
    for goal in shelf_goal:
        if num % 2 == 1:
            act = 'up'
        else:
            act = 'down'
        robot.rotate_to_shelf(shelf)
        robot.run_to_goal(shelf_goal)
        robot.capture_image(shelf)
        robot.capture_action(act)
        robot.capture_image(shelf)
        num += 1


def gogogo(shelf):
    results = robot.get_classify_results(shelf)
    shortest_route = get_shortest_route(results)
    print(shortest_route)

    # Grab and place the objects those are detected
    for block, obj_name in shortest_route.items():
        grab_and_place(obj_name, block)


def run():
    capture_images_of_one_shelf('A')
    gogogo('A')

    for shelf in ['B', 'C', 'D']:
        capture_images_of_one_shelf(shelf)
    gogogo('D')


if __name__ == '__main__':
    import sys
    try:
        if len(sys.argv) > 1:
            shelves = sys.argv[1:]
        else:
            shelves = sys.argv[1]

        for shelf in shelves:
            capture_images_of_one_shelf(shelf)
            gogogo(shelf)
    except:
        time.sleep(10)
        run()
