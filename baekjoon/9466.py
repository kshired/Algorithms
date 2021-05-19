# https://acmicpc.net/problem/9466
# 텀 프로젝트

'''
사이클을 구하는 문제.

'''
import sys
from collections import defaultdict
sys.setrecursionlimit(10**4)
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

T = int(input())
def dfs(now):
    global res
    visit[now] = True
    chk.append(now)

    if not visit[graph[now]]:
        dfs(graph[now])
    else:
        if graph[now] in chk:
            res += chk[chk.index(graph[now]):]
    
for _ in range(T):
    res = []
    graph = defaultdict(int)
    N = int(input())
    visit = [False for _ in range(N+1)]

    for idx, val in enumerate(input_multiple_int()):
        graph[idx+1] = val

    for i in range(1,N+1):
        if not visit[i]:
            chk = []
            dfs(i)
    print(N-len(res))