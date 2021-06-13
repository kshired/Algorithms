def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for idx, price in enumerate(prices):
        if not stack:
            stack.append((price,idx))
        else:
            while stack and stack[-1][0] > price:
                p,i = stack.pop()
                answer[i] = idx-i
            stack.append((price,idx))
            
    while stack:
        p,i = stack.pop()
        answer[i] = len(prices)-i-1
    return answer