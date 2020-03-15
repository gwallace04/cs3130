import random
import timeit 
import math
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

def merge(B: list, C: list) -> list:
    """Merges two sorted arrays into one sorted array"""
    i = 0
    j = 0
    k = 0
    p = len(B)
    q = len(C)
    A = [0] * (p + q)
    while i < p and j < q:
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    if i == p:
        A[k:(p + q + 1)] = C[j:q + 1]
    else:
        A[k:(p + q + 1)] = B[i:q + 1]
    return A

def mergesort(A: list) -> list:
    """
    Sorts a given list with merge sort
    input: A - a list of orderable elements
    output: a list sorted in nondecreasing order
    """
    n = len(A)
    if n > 1:
        f = math.floor(n / 2)
        B = A[0:f]
        C = A[f::]
        B = mergesort(B)
        C = mergesort(C)
        A = merge(B, C)
    return A

def partition(A: list, start: int, end: int) -> int:
    """https://stackabuse.com/quicksort-in-python/"""
    pivot = A[start]
    low = start + 1
    high = end

    while True:
        while low <= high and A[high] >= pivot:
            high = high - 1
        while low <= high and A[low] <= pivot:
            low = low + 1
        if low <= high:
            A[low], A[high] = A[high], A[low]
        else:
            break
    A[start], A[high] = A[high], A[start]

    return high

def quick(A: list, start = 0, end = None) -> list:
    """
    Sorts a given list with merge sort
    input: A - a list of orderable elements
    output: a list sorted in nondecreasing order
    Note: This implementation of quick sort requires passing the start and end
    as parameters due to Python's pass by object reference behavior. To be able
    to call quicksort like the other algorithms, I've overloaded the parameters
    """
    if end == None:
        end = len(A) - 1
    if start >= end:
        return
    p = partition(A, start, end)
    quick(A, start, p - 1)
    quick(A, p + 1, end)
    return A

def wrapper(func, *args, **kwargs):
    """ This is a wrapper to make the timeit call more readable """
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def create_dataset(func_list: list) -> pd.DataFrame:
    num_list = [1000, 10000, 100000]
    lol = list()
    for i in num_list:
        arrays = dict()
        rand = [random.randrange(1, i) for x in range(1, i + 1)]
        arrays["random"] = rand
        sorted = [x for x in range(1, i + 1)]
        arrays["sorted"] = sorted
        almost = [random.randrange(1, i) if x % 10 == 0 else x 
                                         for x in range(1, i + 1)]
        arrays["almost"] = almost
        header = ["alg", "arr_size", "arr_type", "time"]
        for func in func_list:
            for arr_type in arrays.keys(): 
                temp = [func.__name__, i, arr_type]
                wrapped = wrapper(func, arrays[arr_type])
                time = min(timeit.repeat(wrapped, repeat = 5, number = 1))
                temp.append(time)
                lol.append(temp)

    df = pd.DataFrame(lol, columns = header)
    return df

if __name__ == "__main__":
#    A = [x for x in range(1, 10000)]
#    print(quick(A))
    func_list = [bubble, bubble_with_swaps, 
                insertion, selection,
                mergesort]
    df = create_dataset(func_list)
    df.to_csv('results.csv', index=False)
