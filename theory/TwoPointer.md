# Two Pointer And Sliding Window

## 투 포인터

1차원배열에서 2개의 포인터를 조작해가며 원하는 것을 얻으려고 사용 할 때 쓰는 알고리즘.

ex) 2003

```python
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int,input().split())
arr = list(map(int,input().split()))

res = 0
sum = 0
l = 0
h = 0

while True:
    if sum >= M:
        sum -= arr[l]
        l += 1
    elif h == N:
        break
    else:
        sum += arr[h]
        h += 1
    if sum == M:
        res += 1

print(res)
```

- 위 코드에서 lo, hi 는 이 알고리즘에서 말하는 two pointers.
- 위 문제의 제한을 보면, N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)인데 시간제한이 0.5초이므로 일반적인 N중 for문을 사용하면 당연히 **TLE..**
- 그래서 이걸 풀기위해 lo, hi라는 두 개의 포인터를 사용.
- lo, hi는 둘 다 0에서 시작해서 움직임.
  - hi는 뒤로 움직이면, sum에다 값을 더하고
  - lo는 뒤로 움직이면, sum에다 값을 뺌
  - 이런 방식으로 구현을하면 O(N)을 이용하여 위 문제를 풀 수 있음.

## 슬라이딩 윈도우

투 포인터와 거의 유사한 알고리즘.

투 포인터는 연산을 위해 포인터를 이동시키지만, 슬라이딩 윈도우는 **특정 범위를 제한**하여 움직임.

주로 deque을 사용하여 구현.

```python
# https://acmicpc.net/problem/11003
# 최솟값 찾기

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, L = map(int,input().split())
arr = list(map(int,input().split()))
dq = deque()

'''
arr[i-L+1 ~ i]
min
'''

for i in range(N):
    while dq and dq[-1][1] > arr[i]:
        dq.pop()

    dq.append((i,arr[i]))

    while dq and dq[0][0] < i - L + 1:
        dq.popleft()

    print(dq[0][1], end = ' ')
```

1. N개의 배열 값들을 차례로 탐색

2. 탐색 중인 수와 덱에 저장되어 있는 수로 뒤에서부터 비교

3. 만약, 덱에 저장되어 있는 수가 더 클 경우, 범위 내에 최솟값이 될 수 없음. 따라서 전부 pop. 자신보다 큰 수를 차례로 pop하면 자연스럽게 정렬이 될 것.

4. 현재 탐색 중인 수를 인덱스와 함께 저장.

5. 그 후, 덱에 저장되어 있는 수를 앞에서부터 체크하면서 만약 특정 범위 밖에있는 인덱스이면 전부 popleft.

덱에 있는 수를 체크 할 때는, 덱이 비어있는지 아닌지 꼭 확인.

```python
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = {} # val -> idx
        res = 0
        for h, val in enumerate(s):
            if val in d and l <= d[val]:
                l = d[val] + 1
            else:
                res = max(res,h-l+1)
            d[val] = h
        return res

'''
O(N^2)으로 푸는 방법도 있지만,
슬라이딩 윈도우를 이용하면 O(N)을 이용해 해결가능

string의 원소를 순회하면서 dict에 (val,idx)로 저장된 값을 이용해
left, right를 계속 update하고
maximum 값도 update해줌.
'''
```
