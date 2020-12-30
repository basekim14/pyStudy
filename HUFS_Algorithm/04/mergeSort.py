def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2        # p, r의 중간 지점 계산
        merge_sort(A, p, q)     # 전반부 정렬
        merge_sort(A, q+1, r)   # 후반부 정렬
        merge(A, p, q, r)       # 병합

    return                      # A의 요소를 직접 조작하기 때문에 return 값은 필요 없지만
                                # 함수가 끝났음을 명시
def merge(A, p, q, r):
    i = p
    j = q+1
    t = 0
    tmp = [None] * len(A)
    while i <= q and j <= r:

        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1

    while i <= q:
        tmp[t] = A[i]
        t += 1
        i += 1

    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1

    i = p
    t = 0

    while i <= r:
        A[i] = tmp[t]
        i += 1
        t += 1

    return


if __name__ == "__main__":
    A = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    print("========================================================\n")
    print("\t- Merge sort 실행 전 -")
    print("\tA :", A)

    merge_sort(A, 0, len(A) - 1)

    print("\n\t- Merge sort 실행 후 -")
    print("\tA :", A)
    print("\n========================================================")