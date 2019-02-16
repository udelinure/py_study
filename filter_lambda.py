squares = [x ** 2 for x in range(11) if x > 0]
print filter(lambda x : x >= 30 and x <= 70, squares)
