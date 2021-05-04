# https://www.acmicpc.net/problem/1987
# 알파벳

'''
백트래킹시에 꽤나 신경 써야 했던 문제..
예전에 이런 문제 많이 풀었는데 벌써 다 까먹음! ㅎㅎ..

1. bfs는 모든 분기를 다 돌기 때문에, 하나의 정점을 기준으로 끝까지 파는 dfs를 선택.
2. dfs를 더 이상 진행 할 수 없을 때는, 백트래킹이 일어나는 정점들을 다시 방문하지 않았다고 표기해야 함
3. 그래야 백트래킹 이후 다시 dfs를 이용하여 방문 가능하기 때문

참고 : https://mygumi.tistory.com/186
'''

import sys
from collections import deque

sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().rstrip()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(y,x):
    global cnt,ans
    visit[ord(graph[y][x])-ord('A')] = 1
    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if (0<=ny<R) and (0<=nx<C):
            if visit[ord(graph[ny][nx])-ord('A')] == 0:
                cnt += 1
                ans = max(cnt,ans)
                dfs(ny,nx)
    cnt -= 1
    visit[ord(graph[y][x])-ord('A')] = 0


R,C = map(int,input().split())
graph = []
visit = [0 for _ in range(26)]

for _ in range(R):
    graph.append(list(input()))

cnt = 1
ans = 1
dfs(0,0)
print(ans)