# https://acmicpc.net/problem/1005
# ACM Craft

'''
위상정렬 + dp 문제.
1516의 테스트케이스 여러개 추가한 문제.

위상정렬을 진행 한 후,
각 노드에 진입 될 때마다, 이전 차수중 가장 큰 노드의 dp값을 더해주면 된다.

동시의 건설이 가능하다는 조건때문에,
이전 차수의 노드 중 가장 큰 시간을 선택해야 이전 차수가 끝난 직후 건설이 가능하다.
'''

import sys, heapq
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

T = int(input())

for _ in range(T):
    N,K = input_multiple_int()
    g = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    dp = [-1 for _ in range(N+1)]
    hq = []
    weight = list(input_multiple_int())

    for _ in range(K):
        s,e = input_multiple_int()
        g[s].append(e)
        indegree[e] += 1
    
    W = int(input())

    for i in range(1,N+1):
        if indegree[i] == 0:
            heapq.heappush(hq,i)
            dp[i] = weight[i-1]

    while hq:
        popped = heapq.heappop(hq)
        for i in g[popped]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[popped]+weight[i-1])
            if indegree[i] == 0:
                heapq.heappush(hq,i)

    print(dp[W])