# https://programmers.co.kr/learn/courses/30/lessons/68935
# 3진법 뒤집기
# 파이썬은 이런것도 지원한다. 반대로는 안됨. 직접 구현하자.

def solution(n):
    res = ''
    while n:
        res += str(n%3)
        n //= 3
    
    return int(res,3)