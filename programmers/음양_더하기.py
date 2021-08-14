# https://programmers.co.kr/learn/courses/30/lessons/76501
# 음양 더하기

def solution(absolutes, signs):
    return sum(map(lambda x:x[0]*(1 if x[1] else -1),zip(absolutes,signs)))