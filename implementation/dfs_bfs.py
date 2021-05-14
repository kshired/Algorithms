from collections import deque
q = deque()

def dfs(v, graph, visit):
	visit[v] = 1
	print(v)
	for i in range(len(graph)):
		if graph[v][i] == 1 and visit[i] == 0 :
			dfs(i)

def bfs(v, graph, visit):
	q = deque()
	visit[v] = 1
	print(v)
	q.append(v)
	while q:
		v = q.popleft()
		for i in range(len(graph)):
			if graph[v][i] == 1 and visit[i] == 0:
				visit[i] = 1
				print(i)
				q.append(i)