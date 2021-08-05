# https://programmers.co.kr/learn/courses/30/lessons/70129
# 이진 변환 반복하기

def solution(s):
    cnt = 0
    chk = 0
    while len(s) > 1:
        n = sum(map(int,list(s)))
        chk += len(s)-n
        s = bin(n)[2:]
        cnt += 1
        
    return [cnt,chk]