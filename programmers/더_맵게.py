# https://programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게

from heapq import heappop, heappush, heapify

def solution(scoville, K):
    heapify(scoville)
    answer = 0
    
    while scoville[0] < K and len(scoville) > 1:
        s1 = heappop(scoville)
        s2 = heappop(scoville)
        heappush(scoville,s1+s2*2)
        answer += 1
    
    if len(scoville) == 1 and scoville[0] < K:
        answer = -1
    
    return answer