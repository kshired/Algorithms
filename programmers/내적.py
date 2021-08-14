# https://programmers.co.kr/learn/courses/30/lessons/70128
# 내적
# 문제는 쉬운데, 이런 테크닉도 있다는 것을 상기하자.

def solution(a, b):
    return sum(map(lambda x:x[0]*x[1],zip(a,b)))