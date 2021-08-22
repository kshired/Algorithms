# https://programmers.co.kr/learn/courses/30/lessons/17681
# 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        s = bin(arr1[i] | arr2[i])[2:]

        tmp = ' '*(n-len(s))
        for i in s:
            if i == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
        
    return answer