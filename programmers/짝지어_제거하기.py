# https://programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기

def solution(s):
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return 1 if len(stack) == 0 else 0