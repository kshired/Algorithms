# https://programmers.co.kr/learn/courses/30/lessons/12941
# 최솟값 만들기

def solution(A,B):
    return sum([x*y for x,y in zip(sorted(A),sorted(B,reverse=True))])