# https://acmicpc.net/problem/1475
# 방 번호

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

cnt = [0 for _ in range(10)]

for i in input():
    cnt[ord(i)-ord('0')] += 1

nine_six = cnt[9] + cnt[6]

if nine_six % 2 == 0:
    cnt[6] = nine_six // 2
    cnt[9] = nine_six // 2
else:
    cnt[6] = nine_six // 2
    cnt[9] = nine_six // 2 + 1

print(max(cnt))


    