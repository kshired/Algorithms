# https://programmers.co.kr/learn/courses/30/lessons/12899
# 124 나라의 숫자

def solution(n):
    nums = '124'
    answer = ''
    
    while n:
        n -= 1
        div = n // 3
        mod = n % 3
        answer = nums[mod] + answer
        n = div
        
    return answer