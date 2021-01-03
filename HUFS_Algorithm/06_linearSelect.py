from math import ceil

def linear_select(A, p, r, i):
    if p == r:
        return A[p]

    n = len(A)
    if n <= 5:
        return quick_select(A, p, r, i)

    # ⌈n/5⌉개의 그룹에 각각에 대한 중앙값을 담기 위헤
    # 길이가 ceil(n/5)개인 리스트를 선언
    medians = [None] * ceil(n/5)

    # 리스트 A를 원소가 5개인 그룹으로 설정하여 반복문 실행
    # ( 아래 식에 의하여, group이라는 변수에 A의 원소가 5개씩
    #   차례로 들어가게 되고, A의 원소 총수가 5가 아닐 경우에도
    #   리스트 medians의 길이를 적절하게 정하였기 때문에
    #   반복문의 마지막 실행 시의 group의 원소 수는 5개 미만이 됨 )
    # for group in [A[5 * j:5 * (j+1)] for j in range(len(medians))]:
    for j in range(len(medians)):
        group = A[5 * j:5 * (j+1)]
        m = len(group)
        if  m % 5 == 0:
            # group의 원소가 5개이면 3번째 원소가 중앙값,
            medians[j] = quick_select(group, 0, m-1, 3)
        else:
            # group의 원소가 5개 미만이면 두 중앙값 중 임의 선택
            medians[j] = quick_select(group, 0, m-1, (m+1)//2)

    print(medians)

    # 중앙값들 중의 중앙값인 M을 재귀적으로 구함
    # ( 위와 비슷한 원리로, medians의 원소가 홀수면 중앙값, 짝수이면 두 중앙값 중 임의 선택 )
    M = linear_select(medians, 0, len(medians)-1, )

    # 원소가 5개씩인 그룹으로 나누는 아래와 같은 식을
    # list comprehension을 활용하여 축약
    ## groups = []
    ## for j in range(0, n, 5):
    ##     groups.append(A[j:j + 5])
    ## for group in groups:
    # for group in [A[j:j+5] for j in range(0, n, 5)]:
    #     if len(group) % 5 == 0:
    #         medians.append(linear_select(group, 0, len(group)-1, 3))
    #     else:
    #         medians.append(linear_select(group, 0, len(group)-1, (len(group)+1)//2))
    #
    # len(medians)

    # M = linear_select(medians, p, len(medians)-1, (len(medians)+1)//2)
    # print(M)

def quick_select(A, p, r, i):
    if p == r:
        return A[p]

    q = partition(A, p, r)
    k = q-p+1

    if i < k:
        return quick_select(A, p, q-1, i)
    elif i == k:
        return A[q]
    else:
        return quick_select(A, p, q-1, i)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1

if __name__ == "__main__":

    # A = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    # A = [5, 7, 9, 0, 3, 1]
    A = [i for i in range(1, 103)]
    # A = [13, 38, 63, 88]

    print("========================================================\n")

    # print(partition(A, 0, len(A)-1))
    # print(A)

    print("\t- Linear select -")
    # print("\tA :", A)
    result = linear_select(A, 0, len(A)-1, 1)
    print("\n\t리스트 A에서")

    # for i in range(1, len(A)+1):
    #     result = 0
    #     print("\t %s번째로 작은 값 - %s" % (str(i).rjust(2, " "), str(result).rjust(2, " ")))

    print("\n========================================================")