# 20-01-13
# EX 12.5

str1 = input().split()
str2 = input().split()
myDic = {}

if len(str1) <= len(str2):
    lenN = len(str1)
else:
    lenN = len(str2)

for i in range(lenN):
    myDic[str1[i]] = float(str2[i])

print(myDic)
    
