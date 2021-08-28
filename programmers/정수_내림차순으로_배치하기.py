# https://programmers.co.kr/learn/courses/30/lessons/12933
# 정수 내림차순으로 배치하기

def solution(n):
    return int(''.join(reversed(sorted(str(n)))))