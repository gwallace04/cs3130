import random

def bubble(A: list) -> list:
    """
    Sorts a given list with bubble sort
    input: A - a list of orderable elements
    output: a list sorted in nondecreasing order
    """
    n = len(A)
    for i in range(n - 2):
        for j in range(n - 1 - i):
            if A[j + 1] < A[j]:
                A[j], A[j + 1] = A[j + 1], A[j]
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

if __name__ == "__main__":
#    a = [random.randint(0, 100) for iter in range(5)]
    a = list("EXAMPLE")
#    a = [89, 45, 68, 90, 29, 34, 17]
#    selection(a)
    print(bubble(a))

