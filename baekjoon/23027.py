# https://acmicpc.net/problem/23027
# 1번부터 문제의 상태가…?

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

s = input()

def change(s, target, alpha):
    for idx,value in enumerate(s):
        if value in target:
            s[idx] = alpha
    return s

if 'A' in s:
    s = change(list(s),['B','C','D','F'],'A')
elif 'B' in s:
    s = change(list(s),['C','D','F'],'B')
elif 'C' in s:
    s = change(list(s),['D','F'],'C')
else:
    s = list('A'*len(s))

print(''.join(s))
