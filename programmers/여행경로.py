from collections import defaultdict
def solution(tickets):
    routes = defaultdict(list)
    
    for s,e in tickets:
        routes[s].append(e)
    
    for key in routes.keys():
        routes[key].sort(reverse=True)
    
    stack = ['ICN']
    path = []
    while stack:
        begin = stack[-1]
        if begin not in routes or len(routes[begin]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[begin].pop())
    
    return path[::-1]