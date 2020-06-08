# 20-02-27
# EX 31.5

def fib(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

n = int(input())
print(fib(n))
