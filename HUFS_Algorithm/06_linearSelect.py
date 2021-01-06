import math

def linear_select(A, p, r, i):
    len_a = r - p + 1
    if len_a <= 5:
        return quick_select(A, p, r, i)

    # ⌈n/5⌉개의 그룹에 각각에 대한 중앙값을 담기 위헤
    # 길이가 ceil(n/5)개인 리스트를 선언
    medians = [None] * math.ceil(len_a / 5)

    # 리스트 A를 원소가 5개인 그룹으로 설정하여 반복문 실행
    # ( 리스트 medians의 길이를 적절하게 정하였기 때문에
    #   반복문의 마지막 실행 시의 group의 원소 수는 5개 미만이 됨 )
    for j in range(len(medians)):
        group = A[5 * j:5 * (j+1)]
        len_group = len(group)
        # 원소의 개수가 5개일 때 중앙값은 3번째로 선택, 5개 미만일 시
        # ceil함수를 활용하여 적절하게 선택
        # ( ceil(1/2): 1      ceil(2/2): 1        ceil(3/2): 2
        #   ceil(4/2): 2      ceil(5/2): 3 )
        medians[j] = quick_select(group, 0, len_group - 1, math.ceil(len_group / 2))

    # 중앙값들 중의 중앙값인 M을 재귀적으로 구함
    # 이 때, medians의 원소가 홀수면 중앙값, 짝수이면 두 중앙값 중 임의 선택 )
    len_medians = len(medians)
    if len_medians  % 2 != 0:
        M = linear_select(medians, 0, len_medians - 1, (len_medians + 1) // 2)
    else:
        M = linear_select(medians, 0, len_medians - 1, len_medians // 2)

    q = partition_median(A, 0, len(A)-1, M)
    k = q - p + 1

    if i < k:
        return linear_select(A, p, q-1, i)
    elif i == k:
        return A[q]
    else:
        return linear_select(A, q+1, r, i-k)

def quick_select(A, p, r, i):
    if p == r:
        return A[p]

    q = partition_lastvalue(A, p, r)
    k = q - p + 1

    if i < k:
        return quick_select(A, p, q-1, i)
    elif i == k:
        return A[q]
    else:
        return quick_select(A, q+1, r, i-k)

def partition_lastvalue(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def partition_median(A, p, r, M):
    for k in range(len(A)):
        if A[k] == M:
            A[k], A[r] = A[r], A[k]
            return partition_lastvalue(A, p, r)

if __name__ == "__main__":
    A = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    print("========================================================\n")
    print("\t- Linear select -")
    print("\tList : %s\n" % A)
    for i in range(1, len(A)+1):
        print("\t<Test case %d>" % i)
        # 각 루프의 test case에서 원본 리스트의 훼손을 막기 위해 A를 복사한 리스트 사용
        num_list = A[:]
        result = linear_select(num_list, 0, len(num_list) - 1, i)
        print("\t%s번째로 작은 값 - %s\n" % (str(i).rjust(2, " "), str(result).rjust(2, " ")))

    print("========================================================")