# https://acmicpc.net/problem/2631
# 줄세우기

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

'''
이건 아무리 봐도 못풀겠어서 다른 사람의 풀이를 참고했다.

이 문제는 LIS, 최장 부분 증가수열문제다.

그냥 배열의 LIS를 구하고 그 나머지를 한 번씩 잘 옮겨주면 되기 때문에
문제의 답은 N - len(LIS)다.


근데, 이런걸 어떻게 알아채지..
많이 풀면서 익숙해져야겠다.
'''

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp))