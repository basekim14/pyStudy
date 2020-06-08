# 20-02-18
# EX 26.9

a_num, b_num = map(int, input().split())

a = {i for i in range(1, a_num + 1) if a_num % i == 0}
b = {i for i in range(1, b_num + 1) if b_num % i == 0}

divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)
