# https://www.acmicpc.net/problem/1316
# 그룹 단어 체커

N = int(input())
cnt = 0

for _ in range(N):
    string = input().rstrip()
    flag = True
    for i in range(len(string)):
        idx = string.find(string[i],i+1)
        if idx == i+1 or idx == -1:
            continue
        else:
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)