# https://programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호 목록

def solution(phone_book):
    d = dict()
    lens = []
    for phone_num in phone_book:
        d[phone_num] = 1
        lens.append(len(phone_num))
    
    lens = list(set(lens))
    
    for phone_num in phone_book:
        for length in lens:
            if len(phone_num) > length and d.get(phone_num[:length]) :
                return False
    
    return True