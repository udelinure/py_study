A = [[1,1,0],[1,0,1],[0,0,0]]
for i in range(len(A)):
  A[i].reverse()
  for index,elem in enumerate(A[i]):
    A[i][index] = elem ^ 1
print A
