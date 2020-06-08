# 20-03-07
# EX 40.6

def prime_number_generator(start, stop):
    for num in range(start, stop + 1):
        if is_prime(num):
            yield num

def is_prime(n):
    if n < 2:
        return False
    if n is 2:
        return True
    if n % 2 is 0:
        return False

    l = round(n ** 0.5) + 1
    for i in range(3, l, 2):
        if n % i is 0:
            return False
    return True


start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')

