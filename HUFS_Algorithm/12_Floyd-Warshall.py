# 201400270_김건호_#12_Floyd-Warshall.py
# 아랍어과 201400270 김건호

from math import inf
from copy import deepcopy

# 초기 상태의 그래프 A⁰
A = {
    "vertices": [1, 2, 3, 4],
    "edges": [
        # (i번째 정점에서 j번째 정점으로의 거리, i번째 정점, j번째 정점)
        # 자기 자신으로의 거리는 0, 정점 간 이어져있지 않은 경우의 거리는 inf
        (3, 1, 2),
        (inf, 1, 3),
        (5, 1, 4),
        (2, 2, 1),
        (inf, 2, 3),
        (4, 2, 4),
        (inf, 3, 1),
        (1, 3, 2),
        (inf, 3, 4),
        (inf, 4, 1),
        (inf, 4, 2),
        (2, 4, 3),
    ]
}

# 단계별 matrix 출력 -> d0, d1 ... 을 리스트 / 딕셔너리에 담아 result에 출력 후 main에서 값 나타냄

def floyd_warshall(G):
    V = G["vertices"]
    E = G["edges"]
    n = len(V)

    # 알고리즘의 수행 과정을 담을 딕셔너리 result를 선언 후
    # 초기 인접 행렬 A0를 이차원 리스트로 선언 후 result에 삽입
    result = dict()

    A = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            for edge in E:
                if i == edge[1] and j == edge[2]:
                    w = edge[0]
                    A[i-1][j-1] = w
                    break
    else:
        result["A0"] = deepcopy(A)

    for k in range(1, n+1):
        # 알고리즘 수행 단계별로 인접행렬 tmp_A를 선언
        # tmp_A == Aᵏ, prev_A == Aᵏ⁻¹
        # tmp_A = [[0 for _ in range(n)] for _ in range(n)]
        # prev_A = result["A"+str(k-1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                # k행이나 k열에 해당하는 경우와 i와 j가 같은 경우 pass
                if i == k or j == k or i == j:
                    continue

                if k == 1 and i == 2 and j == 3:
                    print(A[i-1][j-1])
                    print(A[i-1][k-1])
                    print(A[k-1][j-1])

                A[i-1][j-1] = min(A[i-1][j-1], A[i-1][k-1] + A[k-1][j-1])
                # tmp_A[i-1][j-1] = min(prev_A[i-1][j-1], prev_A[i-1][k-1] + prev_A[k-1][j-1])

                # d == dᵏᵢⱼ

                # w1 == dᵏ⁻¹ᵢⱼ
                # w1 = prev_A[i-1][j-1]

                # w2 == dᵏ⁻¹ᵢₖ + dᵏ⁻¹ₖⱼ
                # w2 = prev_A[i-1][k-1] + prev_A[k-1][j-1]

                # tmp_A[i-1][j-1] == dᵏᵢⱼ
                # tmp_A[i-1][j-1] = min(w1, w2)
        result["A"+str(k)] = deepcopy(A)
    return result


if __name__ == "__main__":
    result = floyd_warshall(A)

    # 알고리즘의 수행단계(k)별 인접행렬 출력
    for k in range(len(result.keys())):
        key = "A" + str(k)
        superscript = ""
        for token in str(k):
            if token == "0":
                superscript += "⁰"
            elif token == "1":
                superscript += "¹"
            elif token == "2":
                superscript += "²"
            elif token == "3":
                superscript += "³"
            elif token == "4":
                superscript += "⁴"
            elif token == "5":
                superscript += "⁵"
            elif token == "6":
                superscript += "⁶"
            elif token == "7":
                superscript += "⁷"
            elif token == "8":
                superscript += "⁸"
            elif token == "9":
                superscript += "⁹"

        print("%5s =\t" % ("A" + superscript), end="")
        for row in result[key]:
            print("[ ", end="")
            for elem in map(str, row):
                if len(elem) == 1:
                    print(" %s  " % str(elem), end="")
                elif len(elem) == 2:
                    print(" %s " % str(elem), end="")
                else:
                    print("%s " % str(elem), end="")
            print("]", end="\n\t\t")
        print()
