N = 100
parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]

def find(v):
	if v == parent[v]:
		return v
	else:
		u = find(parent[v])
		parent[v] = u
		return u

def merge(u, v):
	u = find(u)
	v = find(v)
	if u == v:
		return True
	if rank[u] > rank[v]:
		u,v = v,u
	parent[u] = v
	if rank[u] == rank[v]:
		rank[v] += 1

def kruskal(edges):
    mst = []
    edges.sort()

    for w, u, v in edges:
        if find(u) != find(v):
            merge(u,v)
            mst.append((w,u,v))
    
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

print(kruskal(edges))