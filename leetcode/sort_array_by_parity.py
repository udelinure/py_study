odd = []
even = []
A = [4,2,5,7]
for number in A:
    if number & 1 == 0:
        even.append(number)
    else:
        odd.append(number)
A[::2] = even
A[1::2] = odd
print A
