def fib(N):
    if N < 2:
        return N
    else:
        return fib(N - 1) + fib(N - 2)
        
print fib(30)
