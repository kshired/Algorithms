# https://programmers.co.kr/learn/courses/30/lessons/42889
# 실패율

def solution(N, stages):
    cnt = [[i,0] for i in range(1,N+1)]
    
    for i in range(1,N+1):
        p,q = 0,0
        for stage in stages:
            if stage >= i:
                q += 1
            if stage == i:
                p += 1
        if q == 0:
            q = 1
        cnt[i-1][1] = p/q
    
            
    cnt.sort(key=lambda x:x[1],reverse=True)
    answer = [val[0] for val in cnt]

    return answer