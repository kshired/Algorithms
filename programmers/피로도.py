# https://programmers.co.kr/learn/courses/30/lessons/87946
# 피로도
# 처음봤을 때 그리디처럼 풀려다가 최대 8개라길래 무지성으로 완전탐색 시켜버림

from itertools import permutations

def solution(k, dungeons):
    val = []
    
    for dungeon in dungeons:
        if dungeon[0] <= k:
            val.append(dungeon)
            
    perms = list(permutations(val,len(val)))
    answer = 0
    
    for perm in perms:
        user_k = k
        tmp = 0
        for req, usage in perm:
            if user_k >= req and user_k >= usage:
                user_k -= usage
                tmp += 1
            if user_k == 0:
                break
        answer = max(answer, tmp)
    
    return answer