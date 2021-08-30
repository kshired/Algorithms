# https://programmers.co.kr/learn/courses/30/lessons/12902
# 3 x n 타일링

def solution(n):
    if n%2:
        return 0
    
    dp = [0 for _ in range(5001)]
    dp[0] = 1
    dp[2] = 3
    dp[4] = 11
    MOD = 1e9+7 
    
    for i in range(6,n+1,2):
        dp[i] = dp[i-2]*3
        for j in range(4,i+1,2):
            dp[i] += dp[i-j]*2
        dp[i] %= MOD
        
    return dp[n]