#!/usr/bin/env python

import heapq


class SquareGrid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 < x < self.width and 0 < y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0:
            results.reverse()   # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super(GridWithWeights, self).__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next_one in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next_one)
            if next_one not in cost_so_far or new_cost < cost_so_far[next_one]:
                cost_so_far[next_one] = new_cost
                priority = new_cost + heuristic(goal, next_one)
                frontier.put(next_one, priority)
                came_from[next_one] = current

    return came_from, cost_so_far, frontier


def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    # path.append(start)
    path.reverse()
    return path


def generate_middle_point(path):
    current = path[0]
    route = []

    # Add the start point
    route.append(current)

    for i in range(len(path)):
        (x, y) = path[i]
        if x != current[0] and y != current[1]:
            route.append(path[i-1])
            current = path[i-1]

    # Add the end point
    route.append(path[len(path)-1])

    return route


def generate_route(path):
    route = []
    for i in range(len(path) - 1):
        (x1, y1) = path[i]
        (x2, y2) = path[i+1]
        if x1 == x2:
            if y1 > y2:
                dirc = 'down'
                route.append((dirc, y1 - y2))
            elif y1 < y2:
                dirc = 'up'
                route.append((dirc, y2 - y1))
        elif y1 == y2:
            if x1 > x2:
                dirc = 'left'
                route.append((dirc, x1 - x2))
            elif x1 < x2:
                dirc = 'right'
                route.append((dirc, x2 - x1))
        else:
            if x1 > x2:
                dirc = 'left'
                route.append((dirc, x1 - x2))
            elif x1 < x2:
                dirc = 'right'
                route.append((dirc, x2 - x1))
            if y1 > y2:
                dirc = 'down'
                route.append((dirc, y1 - y2))
            elif y1 < y2:
                dirc = 'up'
                route.append((dirc, y2 - y1))
    return route


def get_route(start, goal):
    # Construct the map
    diagram = GridWithWeights(12, 12)
    diagram.walls = [(4, 4), (4, 5), (4, 6), (4, 7),
                     (5, 4), (5, 5), (5, 6), (5, 7),
                     (6, 4), (6, 5), (6, 6), (6, 7),
                     (7, 4), (7, 5), (7, 6), (7, 7)]

    came_from, cost_so_far, frontier = search(diagram, start, goal)
    path = reconstruct_path(came_from, start, goal)
    middle_points = generate_middle_point(path)
    route = generate_route(middle_points)
    return route
