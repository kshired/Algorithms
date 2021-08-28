# https://programmers.co.kr/learn/courses/30/lessons/12950
# 행렬의 덧셈

def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]