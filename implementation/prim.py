from collections import defaultdict
from heapq import heappush, heappop, heapify

def prim(start, edges):
    mst = []
    graph = defaultdict(list)
    for w, u, v in edges:
        graph[u].append((w, u, v))
        graph[v].append((w, v, u))
    
    connected = set([start])
    candidated_edge = graph[start]
    heapify(candidated_edge)

    while candidated_edge:
        w, u, v = heappop(candidated_edge)
        if v not in connected:
            connected.add(v)
            mst.append((w, u, v))

            for edge in graph[v]:
                if edge[2] not in connected:
                    heappush(candidated_edge, edge)
    return mst

edges = [
    (7, 1, 2),
    (5, 1, 4),
    (7, 2, 1),
    (8, 2, 3),
    (9, 2, 4),
    (7, 2, 5),
    (8, 3, 2),
    (5, 3, 5),
    (5, 4, 1),
    (9, 4, 2),
    (7, 4, 5),
    (6, 4, 6),
    (7, 5, 2),
    (5, 5, 3),
    (15, 5, 4),
    (8, 5, 6),
    (9, 5, 7),
    (6, 6, 4),
    (8, 6, 5),
    (11, 6, 7),
    (9, 7, 5),
    (11, 7, 6),
]

print(prim(1,edges))