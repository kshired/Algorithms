# https://programmers.co.kr/learn/courses/30/lessons/84325
# 직업군 추천하기

def solution(table, languages, preference):
    d = dict()
    for t in table:
        values = t.split()
        d[values[0]] = 0
        for idx, value in enumerate(values[1:]):
            if value in languages:
                d[values[0]] += preference[languages.index(value)]*(5-idx)
    
    res = sorted(d.items(),key=lambda x:x[1],reverse=True)
    answer = []
    
    for r in res:
        if r[1] == res[0][1]:
            answer.append(r[0])
    answer.sort()
    
    return answer[0]