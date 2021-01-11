# 201400270_김건호_#11_Dijkstra.py
# 아랍어과 201400270 김건호

from math import inf

graph2 = {
    "vertices": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "edges": [
        (10, "A", "C"),
        (8, "B", "A"),
        (9, "B", "D"),
        (11, "B", "F"),
        (2, "C", "E"),
        (6, "D", "A"),
        (1, "D", "C"),
        (3, "D", "F"),
        (4, "E", "H"),
        (8, "F", "G"),
        (8, "F", "H"),
        (12, "G", "D"),
        (5, "G", "E"),
        (7, "H", "G")
    ]
}

# 노드의 알파벳은 과제 #10-1번의 그래프에 적힌 알파벳과 동일함
graph = {
    "vertices": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "edges": [
        (8, "A", "C"),
        (10, "B", "A"),
        (7, "B", "D"),
        (4, "B", "F"),
        (12, "C", "E"),
        (2, "D", "A"),
        (8, "D", "C"),
        (2, "D", "F"),
        (4, "E", "H"),
        (8, "F", "G"),
        (20, "F", "H"),
        (12, "G", "D"),
        (7, "G", "E"),
        (3, "H", "G")
    ]
}

def dijkstra(G, r):
    # 교재 알고리즘과의 일치를 위해 V, E에 값 할당
    V = set(G["vertices"])
    E = G["edges"]
    S = set()
    d = dict()

    for u in V:
        d[u] = inf
    d[r] = 0

    """ test data """
    loop_count = 0

    while S != V:
        loop_count += 1
        print("\n=== %d ===" % loop_count)

        u = extract_min(V-S, d)
        S |= {u}

        # u로부터 연결된 정점들의 집합
        L = {l[2] for l in filter(lambda x: x[1] == u, E)}
        for v in L:
            w = None
            for edge in E:
                if u == edge[1] and v == edge[2]:
                    w = edge[0]

            if (v in V-S) and (d[u] + w < d[v]):
                d[v] = d[u] + w

        print(sorted(d.items()))

    return d

def extract_min(Q, d):
    min_d = inf
    u = None
    for key, value in d.items():
        if (key in Q) and (value < min_d):
            min_d = value
            u = key
    return u

if __name__ == "__main__":
    print(dijkstra(graph, "B"))
