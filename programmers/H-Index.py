def solution(citations):
    citations.sort()
    answer = []
    for idx,val in enumerate(citations):
        if val >= len(citations)-idx:
            return len(citations)-idx
    return 0