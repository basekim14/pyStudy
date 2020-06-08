# 20-01-15
# EX 19.6

num = int(input())

for i in range(num):
    print(' ' * (num - 1 - i), '*' * (2 * i + 1), sep='')
