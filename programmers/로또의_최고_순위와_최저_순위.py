def solution(lottos, win_nums):
    cnt = 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                cnt += 1
    cnt0 = lottos.count(0)
    maximum = 7-cnt-cnt0
    minimum = 7-cnt
    if maximum > 5:
        maximum = 6
    if minimum > 5:
        minimum = 6
    
    answer = [maximum,minimum]
    return answer