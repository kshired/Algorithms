# https://acmicpc.net/problem/4673
# 셀프 넘버

def solve(i):
    return i+sum(map(int,str(i)))

cnt = [False for _ in range(10001)]

for i in range(10001):
    chck = solve(i)
    if solve(i) <= 10000:
        cnt[solve(i)] = True

for i in range(1,10001):
    if not cnt[i]:
        print(i)
