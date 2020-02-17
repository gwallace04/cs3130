"""
PART B: This program uses a iterative algorithm to find the nth Fibonacci number
Author: Gabriel Wallace
"""

def fib_itr(n):
  f_1 = 0
  f_2 = 1
  if n == 0:
    return f_1
  elif n == 1:
    return f_2
  else:
    for i in range(2, n + 1):
      f_3 = f_1 + f_2
      f_1 = f_2
      f_2 = f_3
    return f_2

if __name__ == "__main__":
    print("Let's find the nth Fibonacci number, F_n, iteratively")
    print("Type \"exit\" or \"quit\" to exit\n")
    while True:
        n = input("Enter an integer: ") 
        if n == "exit" or n == "quit":
            break
        print("F_{} = {}".format(n, fib_itr(int(n))))
