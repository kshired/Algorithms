# https://acmicpc.net/problem/1543
# 문서 검색

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

S = input()
find = input()
cnt = 0
i = 0

while i <= len(S)-len(find):
    if S[i:i+len(find)] == find:
        cnt += 1
        i += len(find)
    else:
        i += 1

print(cnt)