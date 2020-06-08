# 20-03-05
# EX 35.6

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))

        # None은 False이므로..
        if 0 <= hour <= 24 and 0 <= minute <= 59 and 0 <= second <= 59:
            return True
        # return (조건식) 형태로도..

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time
        
time_string = input()
if Time.is_time_valid(time_string):
    # 클래스를 리턴받아와야하는 형태
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
