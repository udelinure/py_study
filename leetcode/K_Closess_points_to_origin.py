A = [[1,1],[2,1],[-2,-2]]
def func(x):
  return x[0] ** 2 + x[1] ** 2
A = sorted(A, key = func)
print A[:2]
