class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        arr = [[' ' for _ in range(1000)] for _ in range(numRows)]
        dy = [1,-1]
        dx = [0,1]
        x,y = 0,0
        direction = 0
        for i in s:
            arr[y][x] = i
            if y == numRows-1:
                direction = 1
            elif y == 0:
                direction = 0
            y,x = y+dy[direction], x+dx[direction]
        res = ''
        for i in arr:
            for j in i:
                if j != ' ':
                    res = res+j
        return res