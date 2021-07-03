# # https://acmicpc.net/problem/3190
# # 뱀

# import sys
# input = lambda : sys.stdin.readline().rstrip()
# input_multiple_int = lambda : map(int,input().split())

# N = int(input())
# K = int(input())

# apples = []
# for _ in range(K):
#     apples.append(list(input_multiple_int()))

# L = int(input())
# cmd = dict()
# for _ in range(L):
#     t,c = input().split()
#     t = int(t)
#     cmd[t] = c

# cnt = 0
# snake = [[0,0]]
# dir = [(-1,0),(1,0),(0,-1),(0,1)]
# #       DOWN   UP    LEFT   RIGHT
# cur_dir = 3

# while True:
#     cnt += 1
#     if cmd.get(cnt) == 'L':
#         # R(3) L -> U : 1
#         # U(1) L -> L : 2
#         # L(2) L -> D : 0
#         # D(0) L -> L : 3
#         pass
#     elif cmd.get(cnt) == 'D':
#         # D(0) D -> 
#         # U(1) D ->
#         # L(2) D ->
#         # R(3) D ->
#     else:
#         head = [snake[0][0]+1,snake[0][1]+]
#         snake = 
