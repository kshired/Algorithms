# https://programmers.co.kr/learn/courses/30/lessons/83201
# 상호 평가

def solution(scores):
    answer = []
            
    for i in range(len(scores)):
        max_val = [-1,0]
        min_val = [101,0]
        cnt = 0
        chk = 0
        for j in range(len(scores)):
            if max_val[0] == scores[j][i]:
                max_val[1] += 1
                
            if max_val[0] < scores[j][i]:
                max_val[0] = scores[j][i]
                max_val[1] = 1
            
            if min_val[0] == scores[j][i]:
                min_val[1] += 1
            
            if min_val[0] > scores[j][i]:
                min_val[0] = scores[j][i]
                min_val[1] = 1
            cnt += scores[j][i]
        
        if min_val[1] == 1 and scores[i][i] == min_val[0]:
            chk += 1
            cnt -= scores[i][i]
        if max_val[1] == 1 and scores[i][i] == max_val[0]:
            chk += 1
            cnt -= scores[i][i]
                
                
        val = cnt/(len(scores)-chk)
        
        if val >= 90:
            answer.append('A')
        elif val >= 80:
            answer.append('B')
        elif val >= 70:
            answer.append('C')
        elif val >= 50:
            answer.append('D')
        else:
            answer.append('F')
                
                    
    return ''.join(answer)