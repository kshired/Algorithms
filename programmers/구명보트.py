# https://programmers.co.kr/learn/courses/30/lessons/42885
# 구명보트

def solution(people, limit):
    people.sort()
    answer = 0
    i = 0
    j = len(people)-1
    
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    
    return answer