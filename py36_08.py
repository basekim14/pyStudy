# 20-03-05
# EX 36.8

class AdvancedList(list):
    def replace(self, a, b):
        while a in self:
            self[self.index(a)] = b

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

# self가 리스트 그 자신이 되는 것?
