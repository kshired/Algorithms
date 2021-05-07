# https://www.acmicpc.net/problem/1065
# 한수 

def solve(a):
    a = str(a)
    if len(a) == 1:
        return True
    check = int(a[0]) - int(a[1])
    for i in range(1,len(a)-1):
        if int(a[i]) - int(a[i+1]) != check:
            return False
    return True

N = int(input())

cnt = 0
for i in range(1,N+1):
    if solve(i):
        cnt += 1
print(cnt)