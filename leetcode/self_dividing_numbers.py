'''
left = 1
right = 22
result = range(left,right+1)
list1 = range(left,right + 1)
for k in range(len(list1)):
    temp = [int(i) for i in str(list1[k])]
    for i in temp:
        if i != 0:
            if list1[k] % i != 0:
                result.pop(k)
                break
        else:
            result.pop(k)
            break
print result
'''
def check(k):
    temp = [int(i) for i in str(k)]
    for i in temp:
        if i == 0 or i % k != 0:
            return False
    return True
result = [] 
left = 1
right = 22
for i in range(left,right+1):
    if check(i):
        result.append(i)
print result