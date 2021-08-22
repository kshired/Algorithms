# https://programmers.co.kr/learn/courses/30/lessons/77884/solution_groups?language=python3
# 약수의 개수와 덧셈
# 아무 생각없이 풀었는데, 다시보니 약수의 개수가 짝수 == 제곱수 -> value**0.5 == int(value**0.5)

def find(target):
    cnt = 0
    for i in range(1,target+1):
        if target%i == 0:
            cnt += 1
    return cnt%2 == 0

def solution(left, right):
    answer = 0
    for value in range(left,right+1):
        if find(value):
            answer += value
        else:
            answer -= value
    
    return answer