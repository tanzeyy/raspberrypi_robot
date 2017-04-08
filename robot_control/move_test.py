from move import *
import search

start = (1, 3)
go = Move()
init(go)
while 1:
    w = raw_input('Please input goal-width:')
    h = raw_input('Please input goal-height:')
    goal = (int(w), int(h))
    route = search.get_route(start, goal)
    for way in route:
        go.run(way[0], way[1])
    start = goal
