# https://acmicpc.net/problem/9663
# N-Queen

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

N = int(input())
board = [0 for _ in range(15)]
cnt = 0

'''
board[i] = j -> (i,j)에 퀸을 놓음.

일단 0행 0열부터 N-1열까지 차례로 놓고,
같은 열, 행, 대각선에 있으면 안되니 그것을 판단하고 가지치기

N개까지 전부 판단했다면 cnt를 증가시키고, return
'''
def is_promising(n):
    for i in range(n):
        if board[n] == board[i] or abs(board[n]-board[i]) == n - i:
            return False
    return True

def solve(depth):
    global cnt
    if depth == N:
        cnt += 1
        return
    
    for i in range(N):
        board[depth] = i
        if is_promising(depth):
            solve(depth+1)
    
solve(0)
print(cnt)