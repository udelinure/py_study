A = 5
result = []
for i in bin(5)[2:]:
        result.append(str(int(i) ^ 1))
print int("".join(result),2)
