# https://programmers.co.kr/learn/courses/30/lessons/12924
# 숫자의 표현

def solution(n):
    answer = 0
    for i in range(1,n+1):
        res = 0
        for j in range(i,n+1):
            res += j
            if res == n:
                answer += 1
                break
            if res > n:
                break
    
    return answer