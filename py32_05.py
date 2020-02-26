# 20-02-27
# EX 32.5

files = input().split()
print(list(map(lambda x: x.split('.')[0].zfill(3) + '.' + x.split('.')[1], files)))

