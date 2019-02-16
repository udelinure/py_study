A =  ["cba","daf","ghi"]
result = 0
i = 0
new = []
while i < len(A[0]):
    for m in range(len(A)):
        new.append(A[m][i])
    if new != sorted(new):
        result += 1
    new = []
    i += 1
print result
'''
ct = 0 
for c in zip(*A):
    if sorted(c) != list(c): 
        ct += 1 
print ct
'''