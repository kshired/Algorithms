# https://programmers.co.kr/learn/courses/30/lessons/12929
# 올바른 괄호의 갯수 
# 간단한 dp인줄 알았지만.. 아니였네

def solution(n):
    dp = [0 for _ in range(15)]
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2,15):
        for j in range(1,i+1):
            dp[i] += dp[i-j]*dp[j-1]
    
    return dp[n]