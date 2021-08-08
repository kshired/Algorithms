# https://programmers.co.kr/learn/courses/30/lessons/42842
# 카펫

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(total,2,-1):
        if total % i == 0 :
            j = total // i
            if yellow == (i-2)*(j-2):
                answer = [i,j]
                break
    return answer