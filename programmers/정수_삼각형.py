# https://programmers.co.kr/learn/courses/30/lessons/43105
# 정수 삼각형

def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif i==j:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
    return max(triangle[-1])