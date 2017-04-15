import serial

# Import local modules
import search
from move import *
from dicts import *
from communicate import *

waze = (1, 3)
side = 'right'
go = Mov()

grab_time = 0.8
place_time = 1.5
rotate_time = 1.5
action_time = 1.5
init(go)


def run2goal(goal):
    global waze
    route = search.get_route(waze, goal)
    for way in route:
        go.run(way[0], way[1])
    waze = goal


def runInGrid(route):
    for dirc in route:
        go.moveByTime(dirc, 0.5)


def intoGrid(waze, grid):
    (x1, y1) = waze
    (x2, y2) = grid
    if x1 < x2:
        first = 'right'
        if y1 < y2:
            second = 'up'
        if y1 > y2:
            second = 'down'
        if y1 == y2:
            second = 'no'
    if x1 > x2:
        first = 'left'
        if y1 < y2:
            second = 'up'
        if y1 > y2:
            second = 'down'
        if y1 == y2:
            second = 'no'
    if x1 == x2:
        first = 'no'
        if y1 < y2:
            second = 'up'
        if y1 > y2:
            second = 'down'
        if y1 == y2:
            second = 'no'
    return [first, second]


def exitGrid(route):
    trans = {'up': 'down', 'right': 'left',
             'down': 'up', 'left': 'right',
             'no': 'no'}
    r = map(lambda dirc: trans[dirc], route)
    return r


def classify(shelf):
    rotate2shelf(shelf)
    time.sleep(rotate_time)
    send2pc('capture')
    results = get4results()
    return results


def grab(obj):
    send2arm(obj)
    time.sleep(grab_time)


def place():
    send2arm('D')
    time.sleep(place_time)


def restoreArm():
    send2arm('E')


def armAction(action):
    send2arm(action)
    time.sleep(action_time)


def rotate2cart(cart):
    if cart == '1':
        print(cart)
        send2arm('d')
    if cart == '2' or '3' or '4':
        print(cart)
        send2arm('a')
    if cart == '5' or '6' or '7':
        print(cart)
        send2arm('b')
    if cart == '8' or '9' or '10':
        print(cart)
        send2arm('c')
    time.sleep(rotate_time)


def rotate2shelf(shelf):
    if shelf == 'A':
        send2arm('b')
    if shelf == 'B':
        send2arm('c')
    if shelf == 'C':
        send2arm('d')
    if shelf == 'D':
        send2arm('a')
    time.sleep(rotate_time)


def oneGrabPlace(block, obj_name):
    # Obtain obj information from the Objs class
    obj = getObj(obj_name)
    objGoal = obj.getGoal()
    objPaw = obj.getPaw()
    objCart = obj.getCart()
    objGrid = obj.getGrid()

    # Get the position of the block from the block string
    shelf = block[0:1]
    pos = getPosition(block)
    pre_act = pos[0]
    end_act = pos[1]
    blockGoal = getCoordinates(block)

    rotate2shelf(shelf)
    run2goal(blockGoal)
    armAction(pre_act)
    grab(objPaw)
    armAction(end_act)
    run2goal(objGoal)
    rotate2cart(objCart)
    route = intoGrid(waze, grid)
    runInGrid(route)
    place()
    runInGrid(exitGrid(route))
    restoreArm()


def halfShelf(shelf, side):
    if side == 'right':
        run2goal(right[shelf])
    else:
        run2goal(left[shelf])
    results = classify(shelf)
    for position, obj in results:
        oneGrabPlace(shelf, position, obj)


def oneShelf(shelf):
    for side in ["right", "left"]:
        halfShelf(shelf, side)


def run():
    for shelf in ['A', 'B', 'C', 'D']:
        oneShelf(shelf)
