# https://leetcode.com/problems/minimum-path-sum/
# 64. Minimum Path Sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        
        for i in range(1,len(grid[0])):
            dp[0][i] = grid[0][i] + dp[0][i-1]
            
        for i in range(1,len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
                
        return dp[-1][-1]