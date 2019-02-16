# take second element for sort
def takeSecond(elem):
    return elem[1]
#if u want to use the first element to sort, return elem[0]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# sort list with key
sortedList = sorted(random, key=takeSecond)

# print list
print('Sorted list:', sortedList)

