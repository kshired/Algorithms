# https://programmers.co.kr/learn/courses/30/lessons/92335
# k진수에서 소수 개수 구하기

def mapper(n):
    if len(n) == 0:
        return 0
    else:
        return int(n)
    
def is_prime(n):
    if n == 2:
        return True
    
    if n < 2 or n % 2 == 0:
        return False

    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
        
    return True
        
    
def solution(n, k):
    num = to_k_number(n,k)
    
    numbers = list(map(mapper,num.split('0')))
    
    answer = 0
    
    for number in numbers:
        if is_prime(number):
            answer += 1

    return answer

def to_k_number(n,k):
    res = ''
    while n > 0:
        res += str(n%k)
        n //= k
    return res[::-1]