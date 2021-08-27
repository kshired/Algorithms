# https://programmers.co.kr/learn/courses/30/lessons/12949
# 행렬 곱셈

def solution(arr1, arr2):
    N,M = len(arr1), len(arr2[0])
    
    answer = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k]*arr2[k][j]
            
    
    return answer