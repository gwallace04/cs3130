import random

def gcd_method1(m, n, count = 1):
  # print("gcd({}, {})".format(m, n))
  if n == 0:
    # print("gcd: ", m)
    # print("iterations: ", count)
    return count
  else:
    a = n
    b = m % n
    count += 1
    return gcd_method1(a, b, count)
    
def gcd_method2(m, n, t):
  count = 1
  if m % t == 0 and n % t == 0:
     # print("gcd: ", t)
     # print("iterations: ", count)
     return count
  else:
    t -= 1
    count += 1
    while(t != 0):
      if m % t == 0 and n % t == 0:
        # print("gcd: ", t)
        # print("iterations: ", count)
        return count
        break
      else:
        t -= 1
        count += 1

def main():
  # a = 31415
  # b = 14142
  # a = 34
  # b = 412
  iter1 = 0
  iter2 = 0
  num_sims = 1000000
  for i in range(num_sims + 1):
    a = random.randint(10000, 99999)
    b = random.randint(10000, 99999)
    t = min(a, b)
    iter1 += gcd_method1(a, b)
    iter2 += gcd_method2(a, b, t)
  
  print(iter1 / num_sims, iter2 / num_sims)
  

main()
