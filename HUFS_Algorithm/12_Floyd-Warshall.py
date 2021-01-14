# 201400270_김건호_#12_Floyd-Warshall.py
# 아랍어과 201400270 김건호

from math import inf

# 단계별 matrix 출력 -> d0, d1 ... 을 리스트 / 딕셔너리에 담아 result에 출력 후 main에서 값 나타냄

def floyd_warshall(G):
    n = len(G)

    # 알고리즘의 수행 과정을 담을 딕셔너리 result를 선언 후
    result = dict()


    for i in range(n):
        for j in range(n):
            pass
    return True


if __name__ == "__main__":
    # 2차원 리스트로 구현된 초기 상태 그래프의 인접 행렬 A0
    # 이 때, A[i][j]는 인접 행렬의 i+1행, j+1열을 가리키고,
    # 이에 해당하는 값은 i+1번째 정점에서 j+1번째 정점으로의 거리이다.
    A = [[0, 3, inf, 5],
         [2, 0, inf, 4],
         [inf, 1, 0, inf],
         [inf, inf, 2, 0]]

    # 대상 행렬인 A가 정방행렬인지 확인
    # ( A가 비어있지 않다면 A의 행 개수가 각각의 행 별 요소의 개수와 같은지를 판별 )
    if A and all(map(lambda x: x == len(A), [len(row) for row in A])):
        # target이 정방 행렬일 때 floyd_warshall 함수 호출
        result = floyd_warshall(A)
        print(result)


