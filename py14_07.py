# 20-01-13
# EX 14.7

score = tuple(map(int, input().split()))
sum_val = 0


for i in range(len(score)):
    if 0 <= score[i] <= 100:
        sum_val += score[i]
    else:
        print('잘못된 정수')
        sum_val = -1
        break
    
if sum_val == -1:
    pass
elif sum_val >= 320:
    print('합격')
else:
    print('불합격')
    
