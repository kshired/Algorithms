import sys
sys.setrecursionlimit(10**8)

def solution(n, computers):
    answer = 0
    visit = [False for _ in range(n)]
    
    for i in range(n):
        if not visit[i]:
            dfs(i, visit, computers)
            answer += 1

    return answer

def dfs(v, visit, computers):
    visit[v] = True
    for i in range(len(visit)):
        if computers[v][i] == 1 and not visit[i]:
            dfs(i, visit, computers)