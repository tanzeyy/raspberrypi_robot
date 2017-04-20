#!/usr/bin/env python

# Local modules
from robot import Robot

# Python 2/3 compatibility
from __future__ import print_function
import sys
PY3 = sys.version_info[0] == 3

if PY3:
    from functools import reduce


robot = Robot()


def grab_and_place(obj_name, block):

    # Get the coordinate of detected block
    block_goal = get_coordinates(block)

    # Obtain obj information from the Objs class
    obj = get_obj(obj_name)
    obj_goal = obj.get_goal()
    obj_cart = obj.get_cart()
    obj_grid = obj.get_grid()

    # Actions of grab and place an object
    robot.run_to_goal(block_goal)
    robot.grab_obj(obj_name, block)
    robot.run_to_goal(obj_goal)
    robot.run_in_grid(obj_grid)
    robot.place_obj(obj_name)
    time.sleep(0.8)
    robot.run_in_grid(obj_grid, 'exit')


def half_shelf(shelf, side):

    # Go to the capture point of the shelf
    shelf_goal = get_shelf_side(shelf, side)
    robot.run_to_goal(shelf_goal)

    # Rotate camera to the shelf and take pictures
    robot.rotate_to_shelf(shelf)
    results = robot.classify(shelf, side)

    # Grab and place the objects those are detected
    for block, obj_name in results.items():
        grab_and_place(obj_name, block)


def run():
    for shelf in ['A', 'B', 'C', 'D']:
        for side in ['right', 'left']:
            half_shelf(shelf, side)

# robot.run_to_goal((2, 3), 'fast')
# robot.run_to_goal((3, 3), 'slow')
