def comparison(a,b):
    return len([i for i in range(len(a)) if a[i]!=b[i]]) == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    visit = [False for _ in words]
    s = [begin]
    
    while s:
        val = s.pop()
        if val == target:
            return answer
        
        for i in range(len(words)):
            if comparison(val, words[i]) and not visit[i]:
                visit[i] = True
                s.append(words[i])
        answer += 1
    
    return 0