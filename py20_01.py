# 20-01-15
# EX 20.1

for i in range(1, 101):
    if i % 15 == 0:         # 논리적 의미와 가독성을 위해
        print('FizzBuzz')   # i % 3 and i % 5 를 쓰는 방향으
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
