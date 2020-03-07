# 소수에 관한 공부

def is_prime(n):
    if n < 2:
        return False
    if n is 2:
        return True
    if n % 2 is 0:
        return False

    l = round(n ** 0.5) + 1
    for i in range(3, l, 2):
        if n % i is 0:
            return False
    return True

    '''만약 어떤 자연수 N이 a로 나눠진다면 N = a * b 로 표현할 수 있을 것이다.그렇다면 N 은 a 로도 b 로도 나눠진다는 말이다.즉 이 말은 N의 제곱근 r 을 기준으로 곱해서 N이 될 수 있는 약수들이 같은 개수로 분포한다는 말이다. 따라서 N이 소수인지를 알고 싶으면 N의 제곱근까지만 검사해보면 된다. 이 룰을 추가하는 것만으로 엄청난 시간을 줄일 수 있다.
    '''

def primes_up_to_good(n):
    seive = [False, False] + [True] * (n - 1)
    for k in range(2, int(n ** 0.5 + 1.5):
        if seive[k]:
        seive[k*2::k] = [False] * ((n - k) // k)
    return [x for x in range(n+1) if seive[x]]

# 출처: https://53perc.tistory.com/entry/파이썬-소수-판별하기 [53Percent]

def prime_list(n):
    # True를 소수로 가정
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

#  1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다.
#  2. 2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
#  3. 자기 자신을 제외한 2의 배수를 모두 지운다.
#  4. 남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
#  5. 자기 자신을 제외한 3의 배수를 모두 지운다.
#  6. 남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
#  7. 자기 자신을 제외한 5의 배수를 모두 지운다.
#  8. 남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
#  9. 자기 자신을 제외한 7의 배수를 모두 지운다.
# 10. 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.
#
# 출처 - 위키피디아, 에라토스테네스의 체
