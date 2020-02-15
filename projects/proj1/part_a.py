"""
PART A: This program uses a recursive algorithm to find the nth Fibonacci number
Author: Gabriel Wallace
"""

def fib_rec(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

if __name__ == "__main__":
    print("Let's find the nth Fibonacci number, F_n, recursively")
    n = int(input("Enter an integer: "))
    print("F_{} = {}".format(n, fib_rec(n)))
