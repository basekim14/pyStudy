# 20-01-15
# EX 20.8

start, stop = map(int, input().split())

for i in range(start, stop + 1):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
