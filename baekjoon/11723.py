# https://acmicpc.net/problem/11723
# 집합

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

def add(origin, idx):
    return origin | (1 << idx)

def remove(origin, idx):
    return origin & ~(1 << idx)

def check(origin, idx):
    return 1 if origin & (1 << idx) else 0

def toggle(origin, idx):
    return origin ^ (1 << idx)

def all():
    return 2**21-1

def empty():
    return 0

N = int(input())

origin = 0

for _ in range(N):
    op = input()
    if op[:3] == "all":
        origin = all()
    elif op[:3] == "emp":
        origin = empty()
    elif op[:3] == "add":
        idx = int(op.split()[1])
        origin = add(origin, idx)
    elif op[:3] == "che":
        idx = int(op.split()[1])
        print(check(origin, idx))
    elif op[:3] == "rem":
        idx = int(op.split()[1])
        origin = remove(origin, idx)
    elif op[:3] == "tog":
        idx = int(op.split()[1])
        origin = toggle(origin, idx)

