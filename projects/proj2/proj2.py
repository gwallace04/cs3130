import random
import timeit
import pandas as pd

def bubble(A: list) -> list:
    """
    Sorts a given list with bubble sort
    input: A - a list of orderable elements
    output: a list sorted in nondecreasing order
    """
    n = len(A)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j + 1] < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A


def bubble_with_swaps(A: list) -> list:
    """
    Sorts a given list with improved bubble sort
    input: A - a list of orderable elements
    output: a list sorted in nondecreasing order
    """
    n = len(A)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if A[j + 1] < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
        if not swapped:
            break
    return A

def selection(A: list) -> list:
    """
    Sorts a given list with selection sort
    input: A - a list of orderable elements
    output: a list sorted in nondecreasing order
    """
    n = len(A)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]
    return A

def insertion(A: list) -> list:
    """
    Sorts a given list with insertion sort
    input: A - a list of orderable elements
    output: a list sorted in nondecreasing order
    """
    n = len(A)
    for i in range(1, n):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = v
    return A

def wrapper(func, *args, **kwargs):
    """ This is a wrapper to make the timeit call more readable """
    def wrapped():
        return func(*args. **kwargs)
    return wrapped

def create_dataset(func_list: list) -> pd.DataFrame:
    num_list = [10, 20, 30]
    for i in num_list:
        print(i)
        rand = [random.randrange(1, i) for x in range(1, i + 1)]
        sorted = [x for x in range(1, i + 1)]
        almost = [random.randrange(1, i) if x % 10 == 0 else x 
                                         for x in range(1, i + 1)]



    

if __name__ == "__main__":
    rand = [random.randrange(1, 10) for x in range(1, 10 + 1)]
    create_dataset(rand)

