def quick_select(A, p, r, i):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    k = q - p + 1
    if i < k:
        return quick_select(A, p, q-1, i)
    elif i == k:
        return A[q]
    else:
        return quick_select(A, q+1, r, i-k)

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
    A = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    print("========================================================\n")
    print("\t- Quick select -")
    print("\tList : %s\n" % A)
    for i in range(1, len(A)+1):
        print("\t<Test case %d>" % i)
        # 각 루프의 test case에서 원본 리스트의 훼손을 막기 위해 A를 복사한 리스트 사용
        num_list = A[:]
        result = quick_select(num_list, 0, len(num_list) - 1, i)
        print("\t%s번째로 작은 값 - %s\n" % (str(i).rjust(2, " "), str(result).rjust(2, " ")))

    print("========================================================")