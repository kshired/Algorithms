# https://programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호
# 이제는 식상한 스택으로 괄호처리

def solution(s):
    stack = []
    
    for idx in range(len(s)):
        if s[idx] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            stack.append('(')
    return len(stack) == 0
    