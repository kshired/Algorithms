# https://programmers.co.kr/learn/courses/30/lessons/42628
# 이중우선순위큐

from heapq import heappush,heappop
def solution(operations):
    min_heap = []
    max_heap = []
    
    for operation in operations:
        op, val = operation.split()
        if op == 'I':
            heappush(min_heap,int(val))
            heappush(max_heap,int(val)*-1)
        else:
            if len(min_heap) == 0:
                continue
            if val == '-1':
                min_value = heappop(min_heap)
                max_heap.remove(-min_value)
            else:
                max_value = heappop(max_heap)
                min_heap.remove(-max_value)
    
    if min_heap:
        return [-max_heap[0],min_heap[0]]
    else:
        return [0,0]