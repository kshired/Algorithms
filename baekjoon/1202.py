# https://acmicpc.net/problem/1202
# 보석 도둑

'''
최대 가치의 보석을 담으면서, 용량이 작은 가방부터 채워간다.
'''

import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N,K = input_multiple_int()
hq = []
for _ in range(N):
    weight, value = input_multiple_int()
    heapq.heappush(hq,(weight,value))

bag = []
for _ in range(K):
    heapq.heappush(bag,int(input()))

save = []
res = 0
while bag:
    cur_bag = heapq.heappop(bag)
    # 현재 가방의 용량보다 가벼운 보석들의 가치를 save heap(max heap)에 넣어준다.
    while hq and cur_bag >= hq[0][0]:
        heapq.heappush(save,-heapq.heappop(hq)[1])
    
    # save heap에서 최대 가치의 보석을 가져온다.
    if save:
        res -= heapq.heappop(save)
    elif not hq:
        break

print(res)
