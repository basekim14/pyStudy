# 20-03-02
# EX 33.6

def countdown(n):
    def onesec():
        nonlocal n
        n -= 1
        return n + 1
    return onesec

n = int(input())
c = countdown(n)
for i in range(n):
    print(c(), end=' ')
