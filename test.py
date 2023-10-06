from solution import *
from sokoban import sokoban_goal_state, PROBLEMS
from autograder import *
import os
"""
#
s0 = PROBLEMS[5]  # Problems get harder as i gets bigger
se = SearchEngine('best_first', 'full')
se.init_search(s0, goal_fn=sokoban_goal_state, heur_fn=heur_alternate)
final, stats = se.search(20)
# for i in range(len(PROBLEMS)):
#     print(i)
#     print(heur_alternate(PROBLEMS[i]))
#     print(PROBLEMS[i].print_state())


# for i in range(20):
#     print(i)
#     a, y = weighted_astar(PROBLEMS[i], heur_manhattan_distance, 10, 2)
#     if a:
#         print(a.gval)
#     print(y)

# test_iterative_astar_fun()
# test_iterative_gbfs_fun()
# test_alternate_fun()
len_benchmark = [-99, 19, 21, 20, 9, -99, -99, 41, 15, -99, 73, 49, 62, 39, 38, 160, 139, -99, -99, 207]
# se = SearchEngine('best_first', 'full')
# se.init_search(PROBLEMS[1], goal_fn=sokoban_goal_state, heur_fn=heur_alternate)
# final, stats = se.search(2, (23, 23, 23))
# print(final.gval)
# weighted_astar(PROBLEMS[15], heur_alternate, 10, 2)
# x, y = None, None
# for i in range(20):
#     print(i, "th loop")
#     x, y = weighted_astar(PROBLEMS[i], heur_alternate, 10, 2)
#     if x:
#         print(x.gval)
#     else:
#         print("weight 10 fail")
#     x, y = weighted_astar(PROBLEMS[i], heur_alternate, 2, 2)
#     if x:
#         print(x.gval)
#     else:
#         print("weight 2 fail")
#     se = SearchEngine('best_first')
#     se.init_search(PROBLEMS[i], sokoban_goal_state, heur_alternate)
#     x, y = se.search(2)
#     if x:
#         print(x.gval)
#     else:
#         print("gbfs fail")
#     print(" ")
"""

x = SokobanState("START", 0, None, 5, 4,  # dimensions
             ((0, 1),),  # robots
             frozenset(((1, 2), (2, 2))),  # boxes
             frozenset(((1, 1), (3, 1))),  # storage
             frozenset(((2, 0), (3, 0), (4, 0), (3, 2), (0, 3)))  # obstacles
             )
# x.print_state()
se = SearchEngine('best_first', 'full')
se.init_search(x, goal_fn=sokoban_goal_state, heur_fn=heur_alternate)
final, stats = se.search(20)
while final.parent:
    final.print_state()
    final = final.parent
