# 201400270_김건호_#10_MST.py
# 아랍어과 201400270 김건호
# PrimAlgorithm

from math import inf

""" test data """
graph2 = {
    "vertices": ["A", "B", "C", "D", "E", "F", "G"],
    "edges": [
        ( 8, "A", "B"),
        ( 9, "A", "D"),
        (11, "A", "E"),
        ( 8, "B", "A"),
        (10, "B", "C"),
        (10, "C", "B"),
        ( 5, "C", "D"),
        ( 9, "D", "A"),
        ( 5, "D", "C"),
        (13, "D", "E"),
        (12, "D", "F"),
        (11, "E", "A"),
        (13, "E", "D"),
        ( 8, "E", "G"),
        (12, "F", "D"),
        ( 7, "F", "G"),
        ( 8, "G", "E"),
        ( 7, "G", "F")
    ]
}

# 노드의 알파벳은 과제 #10-1번의 그래프에 적힌 알파벳과 동일함
graph = {
    "vertices": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "edges": [
        (8, "A", "B"),
        (10, "A", "C"),
        (15, "A", "D"),
        (8, "B", "A"),
        (9, "B", "D"),
        (11, "B", "F"),
        (10, "C", "A"),
        (1, "C", "D"),
        (2, "C", "E"),
        (15, "D", "A"),
        (9, "D", "B"),
        (1, "D", "C"),
        (3, "D", "F"),
        (12, "D", "G"),
        (2, "E", "C"),
        (5, "E", "G"),
        (4, "E", "H"),
        (11, "F", "B"),
        (3, "F", "D"),
        (8, "F", "G"),
        (8, "F", "H"),
        (12, "G", "D"),
        (5, "G", "E"),
        (8, "G", "F"),
        (7, "G", "H"),
        (4, "H", "E"),
        (8, "H", "F"),
        (7, "H", "G")
    ]
}

def prim(G, r):
    # 교재 알고리즘과의 일치를 위해 V, E에 값 할당
    V = set(G["vertices"])
    E = G["edges"]
    S = set()
    # L = set()
    d = dict()
    # 알고리즘 이후 신장 트리를 구하기 위해 교재에서 사용한 tree와 달리, # 이 프로그램에서의 tree는
    # 수행 경과와 최종 신장 트리를 제시된 형태에 맞게 출력하기 위해 사용됨
    tree = []


    for u in V:
        d[u] = inf
    d[r] = 0

    """ test data """
    loop_count = 0

    while S != V:

        loop_count += 1
        print("\n=== %d ===" % loop_count)
        u = extract_min(V-S, d)

        # 신장 트리의 요소가 구성될 때마다 경과를 출력하며 리스트 tree에 해당 간선을 저장함
        # 이 때, 집합 S에 하나의 정점만 존재할 때 tree를 구성할 edge가 성립 안되므로, 이 경우를 건너뜀
        if u != r:
            for edge in E:
                if d[u] == edge[0] and u == edge[2]:
                    tree.append(edge)
                    print(tree)
                    break

            # 출력 형태를 맞추기 위한 if 문
            if len(tree) == len(V)-1:
                print()



        S |= {u}
        print("S :", S)

        # u로부터 연결된 정점들의 집합
        L = {l[2] for l in filter(lambda x: x[1] == u, E)}


        # L = set()
        # for vertex in S:
        #     for edge in filter(lambda elem: elem[1] == vertex, E):
        #         if edge[2] not in S:
        #             L.add(edge[2])
        # print("u :", u)
        print("L :", L)

        for v in L:
            # print("v :", v)
            # 정점 u와 v 사이의 거리 w를 구하기 위한 loop
            w = None
            for edge in E:
                if u == edge[1] and v == edge[2]:
                    # print(edge)
                    w = edge[0]

            if (v in V-S) and w < d[v]:
                d[v] = w

        print("d :", d)


        # for elem in L:
        #     v = elem[2]
        #     w = elem[0]
        #     if (v in V-S) and w < d[v]:
        #         d[v] = w

        # tree.append(elem)
        # print(d)
        # print(tree)

    return tree

def extract_min(Q, d):
    # print("Q :", sorted(list(Q)))
    # print("D :", d)

    min_d = inf
    u = None
    for key, value in d.items():
        # if (key in Q):
        #     print(key, value)
        if (key in Q) and (value < min_d):
            min_d = value
            u = key
    return u



def prim2(G, r):
    # 교재 알고리즘과의 일치를 위해 V, E에 값 할당
    V = G["vertices"]
    E = G["edges"]

    tree = []

    # 필요 변수 선언
    Q = V
    d = dict()
    for u in Q:
        d[u] = inf

    d[r] = 0

    while Q:
        u = delete_min(Q, d)
        print("-%s-" % u)
        d.pop(u)
        # 정점 u의 인접 정점과 그에 따른 가중치를 담은 딕셔너리???????
        # L = {l[2]: l[0] for l in filter(lambda x: x[1] == u, E)}
        L = list(filter(lambda elem: elem[1] == u, E))
        for elem in L:
            v = elem[2]
            w = elem[0]
            print(v, w)
            if (v in Q) and w < d[v]:
                d[v] = w
                # tree.append(elem)
        # print(d)
        # print(tree)
        print()
    return

def delete_min(Q, d):
    u = Q.pop(Q.index(min(d)))
    return u

def get_weight(E, u, v):
    return

if __name__ == "__main__":
    print(prim(graph, "A"))