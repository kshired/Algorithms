# https://acmicpc.net/problem/14888
# 연산자 끼워넣기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
arr = list(input_multiple_int())
op = list(input_multiple_int())
res = []

def solve(depth, val):
    if depth == N:
        res.append(val)
        return
    
    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            tmp = val
            if i == 0:
                val += arr[depth]
            elif i == 1:
                val -= arr[depth]
                
            elif i == 2:
                val *= arr[depth]
            else:
                if val*arr[depth] < -1:
                    val = abs(val)//abs(arr[depth])
                    val *= -1
                else:
                    val //= arr[depth]
            solve(depth+1,val)
            val = tmp            
            op[i] += 1


solve(1,arr[0])
print(max(res))
print(min(res))