from search import *
start = (2, 5)
goal = (6, 8)

came_from, cost_so_far = dijkstra_search(diagram, start, goal)
draw_grid(diagram, width=3, point_to=came_from, start=start, goal=goal)
print()
draw_grid(diagram, width=3, number=cost_so_far, start=start, goal=goal)
print()
draw_grid(diagram, width=3, path=reconstruct_path(came_from, start, goal))
path = reconstruct_path(came_from, start, goal)
print(path)
