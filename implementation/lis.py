N = 100000
def LIS(n):
    maxVal = 0

    for i in range(n):
        if i == 0 or lis[-1] < arr[i]:
            lis.append(arr[i])
            trace[i] = len(lis)-1
            maxVal = trace[i]
        else:
            pos = bisect_left(lis, arr[i])
            lis[pos] = arr[i]
            trace[i] = pos
    print(maxVal+1)

    res = []
    for i in range(n-1,-1,-1):
        if trace[i] == maxVal:
            res.append(arr[i])
            maxVal -= 1
    res.reverse()
    print(*res)