# 20-02-19
# EX 27.6

with open('py27_06_txt.txt', 'r') as file:
    s = file.read()
    string = s.split()

for word in string:
    if 'c' in word or 'C' in word:
        print(word.strip(',.'))
