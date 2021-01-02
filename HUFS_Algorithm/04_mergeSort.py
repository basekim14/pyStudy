def quick_sort(A, p, r):
    if p < r:
        q = partition(A,p,r)    # 분할
        quick_sort(A, p, q-1)   # 왼쪽 부분 배열 정렬
        quick_sort(A, q+1, r)   # 오른쪽 부분 배열 정렬
    return                      # A의 요소를 직접 조작하기 때문에 return 값은 필요 없지만
                                # 함수가 끝났음을 명시
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
    print("\t- Quick sort 실행 전 -")
    print("\tA :", A)

    quick_sort(A, 0, len(A) - 1)

    print("\n\t- Quick sort 실행 후 -")
    print("\tA :", A)
    print("\n========================================================")