# 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
def solution(orders, course):
    orders.sort(key=lambda x:len(x))
    
    res = {}
    max_key = {}
    
    for i in course:
        res[i] = []
        max_key[i] = 0
    
    answer = []
    
    s = set()
    
    for menu in orders:
        for c in course:
            for combi in combinations(menu,c):
                s.add(''.join(sorted(combi)))
                
    print(s)
    
    candidate = list(s)
    
    for c in candidate:
        cnt = 0
        for order in orders:
            length = 0
            for value in c:
                if value in order:
                    length += 1
            if length == len(c):
                cnt += 1
        res[len(c)].append((c,cnt))
        max_key[len(c)] = max(cnt,max_key[len(c)])
        
    

    for i in course:
        for val,cnt in res[i]:
            if cnt == max_key[i] and max_key[i] >= 2:
                answer.append(''.join(sorted(val)))
    
    
    answer.sort()
    return answer