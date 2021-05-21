# https://leetcode.com/problems/number-of-islands/
# 200. Number of Islands

import sys
sys.setrecursionlimit(10**7)
class Solution:
    def dfs(self,y,x,visit,grid):
        visit[y][x] = True
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(4):
            ny, nx = y + dir[i][0], x + dir[i][1]
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] == "1" and not visit[ny][nx]:
                    self.dfs(ny,nx,visit,grid)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visit[i][j] and grid[i][j] == "1":
                    res += 1
                    self.dfs(i,j,visit,grid)
        return res