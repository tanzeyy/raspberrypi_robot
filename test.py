from __future__ import print_function


class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")

    def deco(self, func):
        def _deco(self):
            print("start")
            func(self)
            print("over")
        return _deco

    def acquire(self):
        print("locker.acquire() called.")

    def release(self):
        print("  locker.release() called.")


lista = ["no", "right"]
l = filter(lambda dirc: dirc != "no", lista)

waze = (1, 3)


def intoGrid(grid):
    global waze
    (x1, y1) = waze
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
    return filter(lambda dirc: dirc != "no", [first, second])


def fuck(arg):
    print("fuck")
    print(arg)


class Test():
    def __init__(self):
        self.waze = 0

    def run(self):
        self.waze += 1

    def get_waze(self):
        fuck(self.waze)
        return self.waze

t = Test()
t.get_waze()
