# 20-02-19
# EX 27.6

with open('py28_04_txt.txt', 'r') as file:
    s = file.read()
    my_list = s.split()
    
for word in my_list:
    if word == word[::-1]:
        print(word)
