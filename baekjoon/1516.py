# https://www.acmicpc.net/problem/1516
# 게임 개발

import sys, heapq

input = lambda : sys.stdin.readline().rstrip()
pq = []

N = int(input())

graph = [[] for _ in range(N+1)]
weight = [0 for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
dp = [0 for _ in range(N+1)]

for i in range(1,N+1):
    inp = list(map(int,input().split()))
    weight[i] += inp[0]
    for j in inp[1:-1]:
        graph[j].append(i)
        in_degree[i] += 1

for i in range(1,N+1):
    if in_degree[i] == 0:
        heapq.heappush(pq,i)
        dp[i] = weight[i]

while pq:
    popped = heapq.heappop(pq)
    for i in graph[popped]:
        in_degree[i] -= 1
        dp[i] = max(dp[i],dp[popped] + weight[i])
        if in_degree[i] == 0:
            
            heapq.heappush(pq,i)

for i in dp[1:]:
    print(i)