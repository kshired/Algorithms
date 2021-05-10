# https://leetcode.com/problems/surrounded-regions/submissions/
# Surronded Regions

'''
전형적인 dfs, bfs 탐색문제.
O가 경계에만 있지 않으면 전부 X로 바꿀 수 있으니
그냥 O가 경계에 있는지 아닌지 체크하는게 가장 중요.

bfs를 돌면서 경계에 있는지 체크하고,
경계에 있으면 방문은 하지만, 값을 변경하지 않음
경계에 있지않고, 방문하지 않았으며, O인 곳의 좌표는 list에 넣어 
bfs 탐색이 끝난 후 값을 X로 변경해준다.

'''

from collections import deque
class Solution:
    def solve(self, board):
        m,n = len(board), len(board[0])

        visit = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if visit[i][j] or board[i][j] == 'X':
                    continue
                self.bfs(i,j,visit,board)
        
    def bfs(self,y, x, visit, board):
        m,n = len(board), len(board[0])
        q = deque()
        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]
        arr =[]
        isEdge = False
        q.append((y,x))
        visit[y][x] = True
        arr.append((y,x))
        
        while q:
            y,x = q.popleft()
            if y == 0 or y == m-1 or x == 0 or x == n-1:
                isEdge = True
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if (0 <= ny < m) and (0 <= nx < n) and not visit[ny][nx] and board[ny][nx] != 'X':
                    q.append((ny,nx))
                    visit[ny][nx] = True
                    arr.append((ny,nx))
        if isEdge:
            return
        for y,x in arr:
            board[y][x] = 'X' 