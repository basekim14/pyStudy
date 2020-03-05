class Test:
    test_val = 0

    def __init__(self, val):
        self.test_val = val

a = Test(1)
b = Test(2)

print(a.test_val)
print(b.test_val)
print(Test.test_val)
