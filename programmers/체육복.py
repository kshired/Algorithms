# https://programmers.co.kr/learn/courses/30/lessons/42862
# 체육복
# 간단한 그리디 문제.. 문제를 잘 읽자

def solution(n, lost, reserve):
    s_reserve = set(reserve) - set(lost)
    s_lost = set(lost) - set(reserve)
    
    for r in s_reserve:
        if r-1 in s_lost:
            s_lost.remove(r-1)
        elif r+1 in s_lost:
            s_lost.remove(r+1)
                
    
    return n - len(s_lost)