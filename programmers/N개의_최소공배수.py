# https://programmers.co.kr/learn/courses/30/lessons/12953
# N개의 최소공배수

def lcm(n1,n2):
    return n1*n2//gcd(n1,n2)
    
def gcd(n1,n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2,n1%n2)
    
    
def solution(arr):
    answer = arr[0]
    for i in range(1,len(arr)):
        answer = lcm(answer,arr[i])
        
    return answer