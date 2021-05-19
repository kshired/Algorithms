# https://acmicpc.net/problem/2644
# 촌수계산

import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
graph = defaultdict(list)
visit = [False for _ in range(N+1)]
s,e = input_multiple_int()
K = int(input())

def dfs(now,end,cnt):
    cnt += 1
    visit[now] = True
    if now == end:
        print(cnt-1)
        return
    for i in graph[now]:
        if not visit[i]:
            dfs(i,end,cnt)
    
        
for _ in range(K):
    a,b = input_multiple_int()
    graph[a].append(b)
    graph[b].append(a)

dfs(s,e,0)

if not visit[e]:
    print(-1)