

def matrix_path(n, memo={}):
# def matrix_path(n, memo=dict()):
    if (n, n) in memo.keys():
        return memo[(n, n)]

    for i in range(0, n+1):
        memo[(i, 0)] = 0
    for j in range(1, n+1):
        memo[(0, j)] = 0

    return memo[(n, n)]



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
        print(matrix_path(n))
    else:
        print('target 잘못됨')




