# 시간에 관한 공부

while True:
    time = int(input())

    if time <= 0:
        break

    # 23:59:59에서 오버플로우
    time %= 86400 # 24 * 60 * 60

    m, s = divmod(time, 60)
    h, m = divmod(m, 60)

    print('   %d초는 %02d:%02d:%02d' % (time, h, m, s))

print('탐색 종료')
