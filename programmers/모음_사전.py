# https://programmers.co.kr/learn/courses/30/lessons/84512
# 모음_사전
# n개의 중첩된 for문을 재귀로 변환

vowel = ['','A','E','I','O','U']
values = set()

def pick(picked,n):
    global values, vowel
    if n == 0:
        s = []
        for value in picked:
            s.append(vowel[value])
        values.add(''.join(s))
        return
    for i in range(6):
        picked.append(i)
        pick(picked,n-1)
        picked.pop()

def solution(word):
    global values
    
    pick([],5)
    
    values = sorted(list(values))

    for idx in range(len(values)):
        if values[idx] == word:
            return idx
