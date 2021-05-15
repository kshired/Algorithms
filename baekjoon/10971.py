# https://acmicpc.net/problem/10971
# 외판원 순회 2

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
graph = []
visit = [False for _ in range(N)]
path = []
res = 10**9 + 1

for _ in range(N):
    graph.append(list(input_multiple_int()))

def solve(depth):
    global res
    if depth == N:
        weight = 0
        for i in range(len(path)-1):
            if graph[path[i]][path[i+1]] == 0:
                return
            weight += graph[path[i]][path[i+1]]
        
        if graph[path[-1]][path[0]] == 0:
            return
        weight += graph[path[-1]][path[0]]
        res = min(res,weight)
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            path.append(i)
            solve(depth+1)
            path.pop()
            visit[i] = False

solve(0)
print(res)