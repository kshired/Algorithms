# https://www.acmicpc.net/problem/1766
# 문제집

import heapq,sys

input = lambda: sys.stdin.readline().rstrip()

N,M = map(int,input().split())

g = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
pq = []

for i in range(M):
	s,e = map(int,input().split())
	g[s].append(e)
	indegree[e] += 1

for i in range(1,N+1):
	if indegree[i] == 0:
		heapq.heappush(pq,i)

while pq:
	poped = heapq.heappop(pq)
	print(poped,end = ' ')
	for i in g[poped]:
		indegree[i] -= 1
		if indegree[i] == 0:
			heapq.heappush(pq,i)