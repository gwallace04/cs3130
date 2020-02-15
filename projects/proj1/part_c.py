"""
PART C: This program compares the running time of the recursive and the
    iterative algorithms to find the nth Fibonacci number
Author: Gabriel Wallace
"""

import timeit

from part_a import fib_rec
from part_b import fib_itr

def wrapper(func, *args, **kwargs):
    """
    This is a wrapper to make the timeit call more readable
    """
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def create_dataset(some_func, rng: int, *args: str) -> list:
    """
    This functions creates a dataset of the times for some_func to run
    """
    header = [*args]
    lol = [header]
    for i in range(0, rng + 1):
        wrapped = wrapper(some_func, i)
        time = timeit.timeit(wrapped)
        temp = [i, time]
        lol.append(temp)
    return lol

if __name__ == "__main__":
    """
    Create the two datasets for the recursive and iterative algs
    and then output to recursive.csv and iterative.csv
    """
    #Only use 20 for recursive
    rec = create_dataset(fib_rec, 20, "n", "time")
    #Use 100 for iterative
    itr = create_dataset(fib_itr, 100, "n", "time")

