# 20-01-16
# EX 24.6

import string

prices = list(map(int, input().split(';')))

prices.sort(reverse = True)

for i in range(len(prices)):
    print('{0: >9,}'.format(prices[i]))
               
