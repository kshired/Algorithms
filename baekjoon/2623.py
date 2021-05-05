# https://www.acmicpc.net/problem/2623
# 음악프로그램

import heapq,sys

input = lambda: sys.stdin.readline().rstrip()

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
pq = []
res = []

for _ in range(M):
    inp = list(map(int,input().split()))
    n = inp[0]
    s = inp[1]
    for e in inp[2:]:
        graph[s].append(e)
        in_degree[e] += 1
        s = e

for i in range(1,N+1):
    if in_degree[i] == 0:
        heapq.heappush(pq,i)

while pq:
    popped = heapq.heappop(pq)
    res.append(popped)
    for i in graph[popped]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            heapq.heappush(pq,i)

if len(res)==N:
    for i in res:
        print(i)
else:
    print(0)