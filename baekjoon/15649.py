# https://acmicpc.net/problem/15649
# N과 M (1)

'''
대표적인 백트래킹 문제로, visit을 통해 방문여부를 확인한다.
한 원소에서 시작하는 depth에 대한 탐색이 끝나면,
다른 depth에서 그 원소를 사용 할 수 있으니 값들을 다시 초기화하는 것이 중요하다.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N, M = input_multiple_int()

visit = [False for i in range(N)]
res = []

def solve(depth):
    if depth == M:
        for i in res:
            print(i,end=' ')
        print()
    
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            res.append(i+1)
            solve(depth+1)
            res.pop()
            visit[i] = False

solve(0)
    