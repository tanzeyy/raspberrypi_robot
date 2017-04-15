from move import *
import search

start = (1, 3)
go = Mov()
init(go)
while 1:
    for goal in [(3, 3), (2, 9), (10, 8), (3, 3)]:
        route = search.get_route(start, goal)
        for way in route:
            go.run(way[0], way[1])
        start = goal
