from collections import defaultdict
from functools import cmp_to_key

def sorting(x,y):
    if x[0] == y[0]:
        if x[1] < y[1] :
            return -1
        else:
            return 1
    elif x[0] < y[0]:
        return 1
    else:
        return -1

def solution(genres, plays):
    d = defaultdict(list)
    d_sum = defaultdict(int)
    
    for idx in range(len(genres)):
        d[genres[idx]].append((plays[idx],idx))
    
    for key in d.keys():
        d_sum[key] = sum([value[0] for value in d[key]])
        d[key].sort(key=cmp_to_key(sorting))
    
    d_sum = sorted(list(d_sum), key=lambda x:d_sum[x], reverse=True)

    answer = []
    
    for genre in d_sum:
        answer.append(d[genre][0][1])
        if len(d[genre]) > 1:
            answer.append(d[genre][1][1])
        
    
    return answer