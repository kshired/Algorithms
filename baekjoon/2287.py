# https://acmicpc.net/problem/2287
# 모노디지털 표현
'''
dp[i] = i개의 K로 만들 수 있는 수의 set
initialize를 str(K)*i 로 해주고,
4중 for문을 통해서 dp값을 갱신.
그 후 테스트 케이스마다 dp set을 돌면서 최소값을 찾아 출력.
ps) 이 코드를 python3나 pypy3로 제출하면 런타임 에러를 내뱉는다.
이유는 모르겠지만, set에서 문제가 발생하는건지..
같은 방법으로 cpp를 이용해 코드를 작성하면, 에러가 안난다 :()
'''

from collections import defaultdict
import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

dp = defaultdict(set)

K = input()
for i in range(1,9):
    dp[i].add(int(K*i))

K = int(K)

for i in range(1,9):
    for j in range(1,i+1):
        if i + j > 8:
            continue
        for k in dp[i]:
            for l in dp[j]:
                dp[i+j].add(k+l)
                dp[i+j].add(k*l)
                if k != l:
                    dp[i+j].add(abs(k-l))    
                if k > l:
                    dp[i+j].add(k//l)
                else:
                    dp[i+j].add(l//k)

N = int(input())


for _ in range(N):
    res = 9
    val = int(input())
    for i in range(1,9):
        if val in dp[i]:
            res = i
            break
    if res > 8:
        print("NO")
    else:
        print(res)