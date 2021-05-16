'''
부모 정보를 dictionary 형태로 저장 후,
그걸 쭉 따라 올라가면서 다단계로 값을 더해주면 된다.

문제 내용 ㅋㅋㅋㅋㅋ 참..
'''
from collections import defaultdict
def solution(enroll, referral, seller, amount):
    tree = defaultdict(str)
    values = defaultdict(int)
    
    for i in range(len(enroll)):
        tree[enroll[i]] = referral[i]

    
    for i in range(len(seller)):
        now = seller[i]
        value = amount[i]*100
        while now != '-':
            if value < 10:
                values[now] += value
                break
            else:
                values[now] += value-(value//10)
                value = value//10
                now = tree[now]
    
    answer = []
    for i in enroll:
        answer.append(values[i])
    
    return answer