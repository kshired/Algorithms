# https://programmers.co.kr/learn/courses/30/lessons/92341
# 주차 요금 계산

from collections import defaultdict
import math

def get_res(fees, record_dict):
    default_time, default_fee, quantom, quantom_fee = fees
    
    answer = []
    
    for key, values in sorted(record_dict.items(),key=lambda x:x[0]):
        time = values[1]
        fee = 0
        if time <= default_time:
            fee = default_fee
        else:
            fee = default_fee + math.ceil((time-default_time)/quantom) * quantom_fee
            
        answer.append(fee)
    
    return answer 
        
def solution(fees, records):
    last_time = 23*60 + 59
    
    record_dict = defaultdict(list)
    
    
    for record in records:
        time, number, op = record.split()
        h, m = map(int,time.split(':'))
        time = h*60 + m
        
        if op == "OUT":
            record_dict[int(number)][1] += time - record_dict[int(number)][0]
            record_dict[int(number)][0] = -1
        else:
            if len(record_dict[int(number)]) == 0:
                record_dict[int(number)] = [time, 0]
            else:
                record_dict[int(number)][0] = time
    
    for key, value in record_dict.items():
        if value[0] != -1:
            record_dict[key][1] += last_time - value[0]
            record_dict[key][0] = -1
    
    
    return get_res(fees, record_dict)