# https://programmers.co.kr/learn/courses/30/lessons/17682
# 다트 게임

def solution(dartResult):
    dartResult.split()
    answer = []
    
    for idx,value in enumerate(dartResult):
        if value.isdigit():
            if value == '1' and dartResult[idx+1] == '0':
                answer.append(10)
            elif value == '0' and dartResult[idx-1] == '1':
                continue
            else:
                answer.append(int(value))
        elif value in ['S','D','T']:
            if value == 'S':
                answer[-1] = answer[-1] ** 1
            elif value == 'D':
                answer[-1] = answer[-1] ** 2
            elif value == 'T':
                answer[-1] = answer[-1] ** 3
        elif value == '#':
            answer[-1] = answer[-1] * -1
        elif value == '*':
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
    print(answer)
    return sum(answer)