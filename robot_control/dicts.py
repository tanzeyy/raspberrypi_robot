#!/usr/bin/env python

position = {
    'upper': ('U', 'E'), 'lower': ('D', 'Q')
}


def get_position(block):
    if int(block[1:]) % 2 == 0:
        pos = 'lower'
    else:
        pos = 'upper'
    return position[pos]


# Coordinates of the blocks on the shelf
coordinates = {
    'D10': (1, 6), 'D11': (1, 5), 'D12': (1, 5), 'B12': (10, 6), 'B10': (10, 5),
    'B11': (10, 6), 'C9': (6, 10), 'C8': (7, 10), 'C3': (9, 10), 'C2': (10, 10),
    'C1': (10, 10), 'C7': (7, 10), 'C6': (8, 10), 'C5': (8, 10), 'C4': (9, 10),
    'B4': (10, 2), 'B5': (10, 3), 'B6': (10, 3), 'B7': (10, 4), 'B1': (10, 1),
    'B2': (10, 1), 'B3': (10, 2), 'B8': (10, 4), 'B9': (10, 5), 'C12': (5, 10),
    'C11': (5, 10), 'C10': (6, 10), 'A11': (6, 1), 'A10': (5, 1), 'A12': (6, 1),
    'A1': (1, 1), 'A3': (2, 1), 'A2': (1, 1), 'A5': (3, 1), 'A4': (2, 1),
    'A7': (4, 1), 'A6': (3, 1), 'A9': (5, 1), 'A8': (4, 1), 'D8': (1, 7),
    'D9': (1, 6), 'D6': (1, 8), 'D7': (1, 7), 'D4': (1, 9), 'D5': (1, 8),
    'D2': (1, 10), 'D3': (1, 9), 'D1': (1, 10)
}


def get_coordinates(block):
    return coordinates[block]


def get_back_coordinates(block):
    shelf = block[0:1]
    coordinate = coordinates[block]
    if shelf == 'A':
        coordinate = (coordinate[0], coordinate[1] + 1)
    elif shelf == 'B':
        coordinate = (coordinate[0] - 1, coordinate[1])
    elif shelf == 'C':
        coordinate = (coordinate[0], coordinate[1] - 1)
    elif shelf == 'D':
        coordinate = (coordinate[0] + 1, coordinate[1])
    return coordinate


# Objects class
class Objs(object):
    def __init__(self, name, paw, goal, cart, grid):
        self.name = name
        self.paw = paw
        self.goal = goal
        self.cart = cart
        self.grid = grid

    def get_name(self):
        return self.name

    def get_pre_paw(self):
        return self.paw[2]

    def get_paw(self, block):
        if int(block[1:]) % 2 == 0:
            return self.paw[0]
        else:
            return self.paw[1]

    def get_goal(self):
        return self.goal

    def get_cart(self):
        return self.cart

    def get_grid(self):
        return self.grid


# Instances of the objects
yellow_cube = Objs('yellow cube', 'bbj', (5, 3), '1', (5, 3.5))
yakult = Objs('yakult', 'cci', (8, 5), '2', (7.5, 4.5))
jdb = Objs('jdb', '33i', (8, 5), '3', (7.5, 5))
tennis_ball = Objs('tennis ball', '44i', (8, 5), '4', (7.5, 5.5))
mimi = Objs('mimi', '55i', (6, 8), '5', (6.5, 7.5))
wired_ball = Objs('wired ball', '66i', (6, 8), '6', (6, 7.5))
shuttercock = Objs('shuttlecock', '77i', (6, 8), '7', (5.5, 7.5))
mouse = Objs('mouse', '8gi', (3, 6), '8', (3.5, 6.5))
pencil = Objs('pencil', '9fj', (3, 6), '9', (3.5, 6))
pp_ball = Objs('pp ball', 'aei', (3, 6), '10', (3.5, 5.5))


# Get the object with the specified name
def get_obj(name):
    objects = [yellow_cube, yakult, jdb, tennis_ball, mimi,
               wired_ball, shuttercock, mouse, pencil, pp_ball]
    for obj in objects:
        if obj.get_name() == name:
            return obj


class Shelf(object):
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def get_side(self, side):
        if side == 'left':
            return self.left
        if side == 'right':
            return self.right
        else:
            print('Side input error!')

    def get_name(self):
        return self.name


# Instances of the shelves
A = Shelf('A', (5, 2), (2, 2))
B = Shelf('B', (9, 5), (9, 2))
C = Shelf('C', (6, 9), (9, 9))
D = Shelf('D', (2, 6), (2, 9))


def get_shelf_side(shelf, side):
    shelves = [A, B, C, D]
    for slf in shelves:
        if slf.get_name() == shelf:
            return slf.get_side(side)
