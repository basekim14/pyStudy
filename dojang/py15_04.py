# 20-01-14
# EX 15.4

age = int(input())
balance = 9000

if 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
else:
    balance -= 1250

print(balance)
