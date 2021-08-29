# https://programmers.co.kr/learn/courses/30/lessons/12923
# 숫자 블록

def solve(n):
    if n == 1:
        return 0
    for i in range(2,int(n**0.5)+1):
        res = n // i
        if res <= 10 ** 7 and n%i == 0:
            return res
    return 1
    
def solution(begin, end):
    answer = []
    
    for i in range(begin,end+1):
        answer.append(solve(i))
        
    return answer