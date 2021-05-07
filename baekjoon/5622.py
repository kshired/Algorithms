# https://www.acmicpc.net/problem/5622
# 다이얼
alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

cnt = 0
for i in input().rstrip():
    for j in range(len(alpha)):
        if i in alpha[j]:
            cnt += j+3
print(cnt)