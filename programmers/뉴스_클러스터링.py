# https://programmers.co.kr/learn/courses/30/lessons/17677
# 뉴스 클러스터링

def jakard(set1,set2):
    mult = 65536
    a = dict()
    b = dict()
    for key in set1.keys():
        if set2.get(key):
            a[key] = min(set1[key],set2[key])
            b[key] = max(set1[key],set2[key])
        else:
            b[key] = set1[key]
            
    for key in set2.keys():
        if set1.get(key):
            a[key] = min(set1[key],set2[key])
            b[key] = max(set1[key],set2[key])
        else:
            b[key] = set2[key]
    
    a = sum([value for value in a.values()])
    b = sum([value for value in b.values()])
            
    if a == 0 and b == 0:
        return 1*mult
    else:
        return (a*mult)//b
    

def solution(str1, str2):
    set_a = dict()
    set_b = dict()
    
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            if set_a.get(tmp.upper()):
                set_a[tmp.upper()] += 1
            else:
                set_a[tmp.upper()] = 1
                
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if tmp[0].isalpha() and tmp[1].isalpha():
            if set_b.get(tmp.upper()):
                set_b[tmp.upper()] += 1
            else:
                set_b[tmp.upper()] = 1
    
    return jakard(set_a,set_b)
