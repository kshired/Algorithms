# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축

def solution(s):
    if len(s) == 1:
        return 1
    max_split = len(s)
    answer = len(s)
    
    for split in range(1,max_split):
        res = []
        for i in range(0,len(s),split):
            res.append(s[i:i+split])
        answer = min(answer, solve(res))
    return answer

def solve(values):
    dict = [(1,values[0])]
    for i in range(1,len(values)):
        if dict[-1][1] == values[i]:
            dict[-1] = (dict[-1][0]+1, values[i])
        else:
            dict.append((1,values[i]))
    result = 0
    for value, key in dict:
        if value > 1:
            result += len(key) + len(str(value))
        else:
            result += len(key)
    return result