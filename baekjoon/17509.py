# https://acmicpc.net/problem/17509
# And the Winner Is... Ourselves!

import sys
input = lambda : sys.stdin.readline().rstrip()

arr = []
for _ in range(11):
    arr.append(list(map(int,input().split())))

arr.sort()
res = 0
time = 0
for i in arr:
    res += time+i[0]+i[1]*20
    time += i[0]

print(res)
