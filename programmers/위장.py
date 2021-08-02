# https://programmers.co.kr/learn/courses/30/lessons/42578
# 위장 

from collections import defaultdict

def solution(clothes):
    d = defaultdict(list)
    
    for cloth in clothes:
        d[cloth[1]].append(cloth[0])

    answer = 1
    
    for value in d.values():
        answer *= len(value)+1

    return answer - 1