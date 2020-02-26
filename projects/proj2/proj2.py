import random

def selection(A: list) -> list:
    """
    Sorts a given list with selection sort
    input: A - a list of orderable elements
    output: a list sorted in nondecreasing order
    """
    n = len(A)
    for i in range(n):
        min = i
        print(A)
        for j in range(i + 1, n):
            if A[j] < A[min]:
                min = j
            A[i], A[min] = A[min], A[i]

if __name__ == "__main__":
#    a = [random.randint(0, 100) for iter in range(5)]
    a = list("EXAMPLF")
    selection(a)
    print(a)

