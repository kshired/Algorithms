# https://acmicpc.net/problem/1918
# 후위 표기식

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

s = input()
stack = []
op = ['+','-','/','*']
for i in s:
    if i == '(':
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            print(stack.pop(),end='')
        stack.pop()
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(),end='')
        stack.append(i)
    elif i =='+' or i == '-':
        while stack and stack[-1] != '(':
            print(stack.pop(),end='')
        stack.append(i)
    else:
        print(i,end='')
while stack:
    print(stack.pop(),end='')
print()