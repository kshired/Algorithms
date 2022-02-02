# https://programmers.co.kr/learn/courses/30/lessons/92334
# 신고 결과 받기

def solution(id_list, report, k):
    report = list(set(report))
    report_dict = dict()
    
    res_dict = dict()
    
    for id_str in id_list:
        report_dict[id_str] = 0
        res_dict[id_str] = 0
    
    for report_str in report:
        reporter, reported = report_str.split()
        report_dict[reported] += 1
    
    for report_str in report:
        reporter, reported = report_str.split()
        if report_dict[reported] >= k:
            res_dict[reporter] += 1
            
        
    answer = list(res_dict.values())
    return answer