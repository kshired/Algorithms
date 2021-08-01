# Greedy Algorithm

항상 눈 앞의 가장 큰 이익만 좇는 기법.

기준에 따라 좋은 것을 선택하는 알고리즘.

보통 '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 알게 모르게 제시해주는 경우가 많음.

한 번의 선택을 한 이후에도 원래 문제와 동일한 성질들이 성립.

→ 문제의 성질이 동일하게 보존되며, 같은 전략을 반복적으로 취할 수 있는 알고리즘

ex)

```python
# https://acmicpc.net/problem/13904
# 과제

'''
가장 점수가 큰 과제부터 보면서,
그 과제를 가능한 날짜중 최대한 제일 늦게 배치하고,
가능한 날짜가 없으면 포기.
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

arr = []

for _ in range(N):
    d,w = map(int,input().split())
    arr.append((d,w))

arr.sort(key=lambda x:(x[1]),reverse=True)
d = [0 for _ in range(1001)]

for i in arr:
    for j in range(i[0],0,-1):
        if d[j] == 0:
            d[j] = i[1]
            break

print(sum(d))
```

ex)

```python
# https://acmicpc.net/problem/11000
# 강의실 배정
'''
N이 최대 20,000이기 때문에 N^2을 사용하면 TLE
우선순위 큐를 사용해 NlogN의 시간복잡도를 만들자.

힙의 최소 시작시간보다 더 늦거나 같으면 같은 강의실에서 강의를 할 수 있기 때문에,
원래 있던 강의를 삭제하고 새로운 강의를 삽입.

힙의 최소 시작시간보다 더 빠르면 ( 작으면 ) 새로운 강의실에서 해야하므로,
힙에 새로 삽입
'''

import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = []
v = [0 for _ in range(N)]

for _ in range(N):
    s,e = map(int,input().split())
    arr.append((s,e))

arr.sort(key=lambda x:x[0])
hq = []
heapq.heappush(hq,arr[0][1])

for i in range(1,N):
    if hq[0] > arr[i][0]:
        heapq.heappush(hq,arr[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq,arr[i][1])


print(len(hq))
```
