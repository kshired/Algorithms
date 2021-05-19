# https://acmicpc.net/problem/11725
# 트리의 부모 찾기

import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())

parent = [-1 for _ in range(N+1)]
graph = defaultdict(list)

for _ in range(N-1):
    a,b = input_multiple_int()
    graph[a].append(b)
    graph[b].append(a)

s = [1]
parent[1] = 1
parent[0] = 0

while s:
    now = s.pop()
    for i in graph[now]:
        if parent[i] == -1:
            parent[i] = now
            s.append(i)

for i in range(2,N+1):
    print(parent[i])