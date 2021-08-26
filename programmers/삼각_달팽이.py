# https://programmers.co.kr/learn/courses/30/lessons/68645
# 삼각 달팽이

def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    y,x = 0,0
    
    cnt = 1
    cur = 0
    d = [(1,0),(0,1),(-1,-1)]
    while True:
        arr[y][x] = cnt
        dy, dx = y + d[cur][0], x + d[cur][1]
        if 0 <= dy < n and 0 <= dx < n and arr[dy][dx] == 0:
            y,x = dy,dx
        else:
            cur += 1
            cur %= 3
            y,x = y + d[cur][0], x + d[cur][1]
        cnt += 1
        if not(0 <= y < n) or not(0 <= x < n) or arr[y][x] != 0:
            break
    
    answer = []
    for i in range(n):
        for j in range(0,i+1):
            if arr[i][j] != 0:
                answer.append(arr[i][j])
            else:
                break
    
    return answer