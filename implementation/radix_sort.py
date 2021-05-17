from collections import deque

def radix_sort(arr):
    dq = [deque() for _ in range(10)]
    cnt = len(str(max(arr)))

    for i in (10 ** x for x in range(cnt-1)):
        for j in range(len(arr)):
            k = (arr[j]%(i*10))//i
            dq[k].append(arr[j])
        idx = 0

        for j in range(10):
            while dq[j]:
                arr[idx] = dq[j].popleft()
                idx += 1