import timeit

def fib_rec(n):
  if n == 0 or n == 1:
    return n
  else:
    return fib_rec(n - 1) + fib_rec(n - 2)

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
  print("n,time_itr,time_rec")
  for i in range(0, 21):
    time_rec = timeit.timeit("fib_rec(i)", "from __main__ import fib_rec, i")
    time_itr = timeit.timeit("fib_itr(i)", "from __main__ import fib_itr, i")
    print("{},{},{}".format(i, time_itr, time_rec))
  
  
