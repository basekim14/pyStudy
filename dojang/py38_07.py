# 20-03-07
# EX 38.7

class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

def palindrome(word):
    token_list = list(word.lower())
    for token in token_list:
        if not('a' <= token <= 'z'):
            token_list.remove(token)

    # 리스트이터레이터.. '객체'를 반환 ?? map과 함께 추가 공부
    if token_list != list(reversed(token_list)):
        raise NotPalindromeError
    else:
        print(word)

try:
    word = input()
    palindrome(word)
    
except NotPalindromeError as e:
    print(e)
