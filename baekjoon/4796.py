# https://acmicpc.net/problem/4796
# 캠핑

import sys
input = lambda : sys.stdin.readline().rstrip()

case = 1

while True:
    L,P,V = map(int,input().split())
    if L == 0:
        break

    if V % P > L:
        print(f'Case {case}: {V//P*L+L}')
    else:
        print(f'Case {case}: {V//P*L+V%P}')
    
    case += 1