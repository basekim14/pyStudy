# 201400270_김건호_#08_matrixPath.py
# 아랍어과 201400270 김건호

# 튜플 (i, j)쌍을 키로 갖는 dictionary 선언
# 교재 알고리즘 상의 c[i, j]는 memo[(i, j)]와 같음
memo = dict()

def matrix_path(n):
    for i in range(0, n+1):
        memo[(i, 0)] = 0
    for j in range(1, n+1):
        memo[(0, j)] = 0

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 and j == 1:
                memo[(1, 1)] = get_target_value(1, 1)
            elif i == 1 and j > 1:
                memo[(1, j)] = get_target_value(1, j) + memo[(1, j-1)]
            elif i > 1 and j == 1:
                memo[(i, 1)] = get_target_value(i, 1) + memo[(i-1, 1)]
            else:
                memo[(i, j)] = get_target_value(i, j) + min((memo[(i-1, j)], memo[i, j-1]))

    # 제시하는 출력 형태를 맞추기 위해 단일 값이 아닌 dictionary 자체를 return
    return memo

# 대상 행렬의 값을 구하는 함수로, matrix_path 코드 내부의 가독성을 위해 사용
def get_target_value(i, j):
    return target[j-1][i-1]

if __name__ == "__main__":
    target = [[ 6,  7, 12,  5],
              [ 5,  3, 11, 18],
              [ 7, 17,  3,  3],
              [ 8, 10, 14,  9]]

    # 대상 행렬인 target이 정방행렬인지 확인
    # ( target이 비어있지 않다면 target의 행 개수가 각각의 행 별 요소의 개수가 같은지를 판별 )
    if target and all(map(lambda x: x == len(target), [len(row) for row in target])):
        # target이 정방 행렬이므로 n의 값을 아래와 같이 산정할 근거가 됨
        n = len(target)
        result = matrix_path(n)

    if result:
        # 행렬 최소 경로 값 출력
        print("행렬 최소 경로 값:\t%d" % result[(n, n)])

        # 대상 행렬의 각 원소에 이르는 최소값 출력
        for j in range(1, n + 1):
            tmp = []
            for i in range(1, n + 1):
                tmp.append(result[(i, j)])
            print(tmp)

        # 경로(행, 열) 출력
        print("경로(행, 열):")
        i = 1
        j = 1
        while True:
            print("%d , %d" % (j-1, i-1))
            # 경로상 위치에서 값의 크기에 따라 우향 이동과 하향 이동이 모두 가능한 경우
            if i < n and j < n:
                if result[(i, j + 1)] < result[(i + 1, j)]:
                    j += 1
                else:
                    i += 1
            # 경로상 위치가 최종 목적지인 경우(마지막 경로에 도달했을 경우)
            elif i == n and j == n:
                break
            # 경로상 위치가 최대 i값 지점에 도달하여 하향 이동만 가능한 경우
            elif i == n and j > 0:
                j += 1
            # 경로상 위치가 최대 j값 지점에 도달하여 우향 이동만 가능한 경우
            elif i > 0 and j == n:
                i += 1
            # 위의 조건에 해당하지 않는 경우(i값이나 j값 중 하나가 n값을 초과한 경우로, 구현상의 오류)
            else:
                print("경로 탐색 오류 발생")
                break
    else:
        print("\ttarget 행렬 오류")
