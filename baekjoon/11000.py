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