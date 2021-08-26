# https://programmers.co.kr/learn/courses/30/lessons/17686
# 파일명 정렬

def get_num(s):
    res = ''
    flag = False
    for val in s:
        if val.isdigit():
            flag = True
            if int(res+val) > 99999 or len(res) == 5:
                break
            else:
                res += val
        else:
            if flag:
                break
    return int(res)

def get_head(s):
    res = []
    for val in s:
        if val.isdigit():
            break
        else:
            res.append(val)
    return ''.join(res).upper()
        
def solution(files):
    files.sort(key=lambda x:(get_head(x),int(get_num(x))))
        
    return files