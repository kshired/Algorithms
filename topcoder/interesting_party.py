def best_invitation(first, second):
    d = dict()
    
    for i in range(len(first)):
        d[first[i]] = 0
        d[second[i]] = 0
    
    for i in range(len(first)):
        d[first[i]] += 1
        d[second[i]] += 1
    
    return max(d.values())