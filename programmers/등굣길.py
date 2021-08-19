# https://programmers.co.kr/learn/courses/30/lessons/42898
# 등굣길
# 고등학생 때 많이 풀었던 조합 문제.. 이게 dp 였네!

def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    MOD = 1e9+7
    for puddle in puddles:
        y,x = puddle
        dp[x-1][y-1] = -1
    
    flag = False
    for i in range(1,n):
        if dp[i][0] != -1 and not flag:
            dp[i][0] = 1
        else:
            flag = True
    
    flag = False
    for i in range(1,m):
        if dp[0][i] != -1 and not flag:
            dp[0][i] = 1
        else:
            flag = True
    
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] != -1:
                if dp[i-1][j] == -1:
                    dp[i][j] = dp[i][j-1] 
                elif dp[i][j-1] == -1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
    
    return int(dp[-1][-1]%MOD)