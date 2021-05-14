import heapq,sys

input = lambda: sys.stdin.readline().rstrip()

N,M = map(int,input().split())

g = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
pq = [] # mean heap

# 그래프 초기화 및 진입차수 설정
for i in range(M):
	s,e = map(int,input().split())
	g[s].append(e)
	indegree[e] += 1

# 진입차수가 0인 것들부터 heap에 push
for i in range(1,N+1):
	if indegree[i] == 0:
		heapq.heappush(pq,i)

while pq:
	poped = heapq.heappop(pq)
	print(poped,end = ' ')
    
    # 정점에서 연결되어 있는 다른 정점 방문 후 진입차수 낮추기
	for i in g[poped]:
		indegree[i] -= 1
		if indegree[i] == 0:
			heapq.heappush(pq,i)