# https://programmers.co.kr/learn/courses/30/lessons/12905
# 가장 큰 정사각형 찾기

def solution(board):
    res = 0
    dp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            dp[i][j] = board[i-1][j-1]
    
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if dp[i][j] == 1:
                dp[i][j] = min((dp[i-1][j-1],dp[i-1][j],dp[i][j-1]))+1
                res = max(dp[i][j], res)
    
    return res**2