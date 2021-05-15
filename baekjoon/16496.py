# https://acmicpc.net/problem/16496
# 큰 수 만들기

import sys
import functools
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

n = int(input())
arr = [ i for i in input().split()]
cmp = lambda x,y:int(x+y)-int(y+x)

arr.sort(key=functools.cmp_to_key(cmp),reverse=True)
print(''.join(arr))