# Dynamic Programming

동적계획법이라고 불리는 dp 알고리즘은 dynamic과 **아무 상관이 없음.**

한국어로는 **메모하며 풀기**가 더 맞는 번역.

이미 계산한 값을 반복하여 계산하지않고, 저장해놓은 값(메모한 값)에서 가져와 시간복잡도를 줄이는 기법.

주어진 문제를 여러 개의 **부분 문제**들로 나누어 푼 다음, 그 결과들로 주어진 문제를 푼다. 부분문제에서 겹치는 것들은 memo를 해놓고 거기서 시간복잡도를 줄인다.

ex)

fibonacci를 재귀로 구현하면 다음과 같다

```python
def f(n):
    if n <= 1:
        return n
    return f(n-2) + f(n-1)
```

만약에 f(10)을 호출한다하면, 이미 호출한 f(0) ~ f(8)을 중복적으로 여러번 호출하게 된다.

n = 10일 때는 값이 작아보일 수 있지만, n이 커지면 f(0)등을 중복적으로 호출하는 횟수가 지수적으로 많아지기 때문에 이것을 해결할 방법으로 dp를 사용하자.

```
10
F(10): 55
호출 횟수
F(0): 34회 호출
F(1): 55회 호출
F(2): 34회 호출
F(3): 21회 호출
F(4): 13회 호출
F(5): 8회 호출
F(6): 5회 호출
F(7): 3회 호출
F(8): 2회 호출
F(9): 1회 호출
F(10): 1회 호출
```

ex) fibonacci를 dp로 구현 ( top-down, 재귀 )

```python
memo = [-1 for _ in range(N+1)]
memo[0] = 0
memo[1] = 1

def fibo(n):
	# 이미 계산해놓은 값은 다시 계산하지않고, 저장해놓은 값에서 가져와서 return
	if memo[n] != -1:
		return memo[n]
	else: # 아니라면, 계산후 memo하고 return
		memo[n] = fibo(n-1) + fibo(n-2)
		return memo[n]

N = int(input())
print(fibo(N))
```

ex) fibonacci를 dp로 구현 ( bottom-up, 반복문 )

```python
N = int(input())
memo = [0 for _ in range(N+1)]
memo[1] = 1

for i in range(2,N+1):
	memo[i] = memo[i-1] + memo[i-2]

print(memo[N])
```

ex) 1463, 1로 만들기

bottom-up

```python
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
dp = [10**8 for _ in range(10**6+1)]
dp[1] = 0
for i in range(1,N):
    dp[i+1] = min(dp[i+1],dp[i] + 1)
    if i*3 <= N:
        dp[i*3] = min(dp[i*3],dp[i] + 1)
    if i*2 <= N:
        dp[i*2] = min(dp[i*2],dp[i] + 1)

print(dp[N])
```

top-down

재귀로 풀면 이렇게 풀리지만, 메모리초과가 난다. N이 최대값이면, 재귀 깊이가 아마 최소 10\*\*6까지 들어가서 그런 듯.

```python
import sys
sys.setrecursionlimit(10**7)

N = int(input())
dp = [-1 for _ in range(N+1)]
dp[1] = 0

def solve(n):
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = solve(n-1) + 1
        if n % 3 == 0:
            dp[n] = min(dp[n], solve(n//3) + 1)
        if n % 2 == 0:
            dp[n] = min(dp[n], solve(n//2) + 1)
        return dp[n]

print(solve(N))
```

### 2종류의 LCS

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e0b453f1-7ac3-4910-b239-cd93ff55e8c2/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e0b453f1-7ac3-4910-b239-cd93ff55e8c2/Untitled.png)

**LCS(Longest Common Substring, 최장 공통 문자열)**

```python
'''
if s1[j] == s2[i]:
	dp[i][j] = dp[i-1][j-1] + 1
else:
	dp[i][j] = 0
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

s1 = '0'+input()
s2 = '0'+input()

N,M = len(s1), len(s2)

dp = [[0 for _ in range(N)] for _ in range(M)]

for i in range(1,M):
    for j in range(1,N):
        if s1[j] == s2[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = 0

print(max([max(i) for i in dp]))

# Substring 출력
length = max([max(i) for i in dp])
end = -1
flag = False
for i in range(1,M):
	for j in range(1,N):
		if dp[i][j] == length:
			flag = True
			end = j
			break
	if flag:
		break

print(s1[end+1-length:end+1])
```

**LCS(Longest Common Subsequence, 최장 공통 부분 수열)**

```python
'''
if s1[j] == s2[i]:
	dp[i][j] = dp[i-1][j-1] + 1
else:
	dp[i][j] = max(dp[i-1][j], dp[i][j-1])
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

s1 = '0'+input()
s2 = '0'+input()

N,M = len(s1), len(s2)

dp = [[0 for _ in range(N)] for _ in range(M)]

for i in range(1,M):
    for j in range(1,N):
        if s1[j] == s2[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(max(dp[M-1]))
```
