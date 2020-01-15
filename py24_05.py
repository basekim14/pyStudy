# 20-01-16
# EX 24.5

import string

sentence ='the grown-ups\' response, this time, was to advise me to lay aside \
          my drawings of boa constrictors, whether from the inside or the \
          outside, and devote myself instead to geography, history, arithmetic, \
          and grammar. That is why, at the, age of six, I gave up what might \
          have been a magnificent career as a painter. I had been disheartened \
          by the failure of my Drawing Number One and my Drawing Number Two. \
          Grown-ups never understand anything by themselves, and it is \
          tiresome for children to be always and forever explaining things to \
          the.'

my_list = sentence.split()

for i in range(len(my_list)):
    my_list[i] = my_list[i].strip(string.punctuation).lower()

count = 0

for word in my_list:
    if word == 'the':
        count += 1

print(count)
