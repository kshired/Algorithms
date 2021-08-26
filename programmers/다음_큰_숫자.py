# https://programmers.co.kr/learn/courses/30/lessons/12911
# 다음 큰 숫자

def count(n):
    cnt = 0
    while n != 0:
        n &= n-1
        cnt += 1
    return cnt

def solution(n):
    cnt = count(n)
    cur = n + 1
    while True:
        if cnt == count(cur):
            return cur
        cur += 1