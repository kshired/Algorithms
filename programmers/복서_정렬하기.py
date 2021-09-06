# https://programmers.co.kr/learn/courses/30/lessons/85002
# 복서_정렬하기

def get_win_rate(win):
    cnt, tot = win
    if tot == 0:
        return 0
    return cnt/tot*100


def solution(weights, head2head):
    N = len(weights)
    win = [[0,0] for _ in range(N)]
    win_heavy = [0 for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if head2head[i][j] == 'W':
                win[i][0] += 1
                win[i][1] += 1
                if weights[i] < weights[j]:
                    win_heavy[i] += 1
            elif head2head[i][j] == 'L':
                win[i][1] += 1
            else:
                continue
    
    
    answer = [i for i in range(1,N+1)]
    
    answer.sort(key=lambda x:(get_win_rate(win[x-1]),win_heavy[x-1],weights[x-1],-x), reverse=True)
    
    return answer
