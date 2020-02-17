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
    print("Type \"exit\" or \"quit\" to exit\n")
    while True:
        n = input("Enter an integer: ") 
        if n == "exit" or n == "quit":
            break
        print("F_{} = {}".format(n, fib_rec(int(n))))
        
