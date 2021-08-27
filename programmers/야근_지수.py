# https://programmers.co.kr/learn/courses/30/lessons/12927
# 야근 지수

from heapq import heappush,heappop,heapify
def solution(n, works):
    works = [-work for work in works]
    heapify(works)
    for i in range(n):
        if len(works) == 0:
            break
        value = heappop(works)
        if abs(value) > 1:
            heappush(works,-(abs(value)-1))

    answer = 0
    
    for value in works:
        answer += value**2
        
    return answer