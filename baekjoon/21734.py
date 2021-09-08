# https://acmicpc.net/problem
# SMUPC의 등장

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

string = input()

for char in string:
    cnt = sum([int(i) for i in str(ord(char))])
    print(char*cnt)