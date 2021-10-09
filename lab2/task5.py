def fib(arg):
    if arg in (1, 2):
        return 1
    return fib(arg - 1) + fib(arg - 2)


n = int(input())
print(fib(n))
