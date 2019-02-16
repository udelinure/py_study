def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
n = raw_input("pls input the number u want to calculate ")
print fact(int(n))