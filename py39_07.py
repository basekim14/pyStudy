# 20-03-07
# EX 39.7

class TimeIter:
    def __init__(self, start, stop):
        self.start = stop
        self.stop = stop

    def __getitem__(self, index):
        if start + index < self.stop:
            
            return self.calc_time(start + index)
        else:
            raise IndexError

    def calc_time(self, time):
        time %= 86400 # 24 * 60 * 60
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        return '%02d:%02d:%02d' % (h, m,s)

start, stop, index = map(int, input().split())

for i in TimeIter(start, stop):
    print(i)

print(TimeIter(start, stop)[index])


'''
# 하루를(24시) 넘지 않는 경우


import datetime
mydelta = datetime.timedelta(seconds=666)
mytime = datetime.datetime.min + mydelta #datetime.datetime은 년/월/일까지 계산하게 돼서 24시가 넘는 h는 일(day)로 변환됩니다.
h, m, s = mytime.hour, mytime.minute, mytime.second

# 하루를 넘기는 경우

m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print "%d:%02d:%02d" % (h, m, s)
'''
