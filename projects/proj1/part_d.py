
def add_digits(a: list, b: list) -> list: 
  carry = 0
  max_size = max(len(a), len(b))
  c = [None] * max_size
  a.extend([0] * (len(b) - len(a)))
  b.extend([0] * (len(a) - len(b)))
  for i in range(0, max_size):
    c[i] = (a[i] + b[i] + carry) % 10
    carry = (a[i] + b[i] + carry) // 10
  if carry != 0:
    c.append(carry)
  return c

def fib_with_n_digits(n: int) -> list:
  a = [0]
  b = [1]
  while (len(b) < n + 1):
    c = add_digits(a, b)
    a = b
    b = c
  return a


if __name__ == "__main__":
  fib_list = fib_with_n_digits(1000)
  fib_string = ''.join(map(str, fib_list))
  fib_string = fib_string[::-1]
  print(fib_string)
