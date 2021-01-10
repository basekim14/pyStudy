# 201400270_김건호_#09_matrixChainMultiplication.py
# 아랍어과 201400270 김건호

# 튜플 (i, j)쌍을 키로 갖는 dictionary 선언
# 강의에서 다룬 예제 3.6의 M[i][j]는 M[(i, j)]와 같음
# e.g. M[1][2] == M[(1, 2)]
M = dict()

# 행렬곱 A1...AN의 최소 비용을 구하는 함수로,
# 교재 알고리즘의 매개변수 i, j 대신 행렬의 개수를 나타내는 변수 N을 사용
# 이 때, i == 1이고 j == N이므로 matrix_chain(i, j)는 matrix_chain(N)과 같음
def matrix_chain(N):
    for i in range(1, N + 1):
        M[(i, i)] = 0

    # 몇 번째 대각선임을 나타내는 제어변수 r
    for r in range(1, N):
        for i in range(1, N - r + 1):
            j = i + r
            values = [M[(i,k)] + M[(k+1, j)] + p[i-1] * p[k] * p[j] for k in range(i, j)]
            M[(i, j)] = min(values)

    return M[(1, N)]


if __name__ == "__main__":
    # 행렬의 개수 입력
    N = int(input())

    # 행렬의 크기를 나타내기 위한 값을 담는 리스트 p 선언
    # 이 때, 행렬 A1, A2, ..., An은 각각 p[0]*p[1], p[1]*p[2], ..., p[n-1]*p[n] 행렬임
    p = [None] * (N + 1)

    for i in range(N):
        # 행렬의 크기를 A * B라 할 때, 크기 값이 잘못 입력되는 경우를 검사하는 식을 추가
        A, B = map(int, input().split())
        if p[i]:
            if p[i] == A:
                p[i+1] = B
            else:
                print("잘못된 행렬 크기 입력")
                exit(0)
        else:
            # p[i], p[i+1] 위치에 A, B를 저장하는 것과 같음
            p[i] = A
            p[i+1] = B

    print(matrix_chain(N))



