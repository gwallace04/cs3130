"""
filename: part_b.py
author: Gabriel Wallace
Gets the average height of binary search trees of various sizes
"""

import random

from bst import Tree, Node

def get_avg_height(N: int, t: int, print_statements=False) -> float:
    height_sum = 0
    for i in range(t):
        rand = [random.randrange(1, 501) for x in range(N)]
        tree = Tree()
        for x in rand:
            tree.insert(x)

        height_sum += tree.height()
        if print_statements:
            print("The height of the tree is", tree.height())
    avg = height_sum / t 
    if print_statements:
        print("The average height is", avg)
    return avg
        

if __name__ == "__main__":
    print(get_avg_height(100, 5, print_statements=True))

    for N in [100, 500, 1000]:
        for t in [5, 10, 15]:
            print("{}, {}, {}".format(
                N, t, get_avg_height(N, t)))
