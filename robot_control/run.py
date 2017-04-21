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


# robot.run_to_goal((2, 3), 'fast')
# robot.run_to_goal((3, 3), 'slow')
