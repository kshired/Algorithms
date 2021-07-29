# 합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413
# 문제 그림만 봐도 그래프 최단거리
# 다익스트라로 해결하던지, 숫자가 작으니 플로이드 와샬로 해결

def solution(n, s, a, b, fares):
    dp = [[2e7+1 for _ in range(n+1)] for _ in range(n+1)]
    
    for fare in fares:
        u,v,value = fare
        dp[u][v] = value
        dp[v][u] = value
    
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                dp[i][j] = 0
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dp[i][j] > dp[i][k]+dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    
    answer = 1e9+7
    
    for i in range(1,n+1):
        answer = min(answer,dp[s][i]+dp[i][a]+dp[i][b])
    
    return answer