# https://acmicpc.net/problem/8279
# Double Factorial

'''
하루종일 풀었던 문제.. 실력좀 키워야겠다 :(

n의 크기가 10^18이기 때문에, log 시간 복잡도로 풀어야한다.

5의 k승씩 그룹화하여 group*pos + sigma{1}{group-1}*5**n을
해주는 방법을 반복하여 count 해주면 된다.

k은 1부터 시작하며 n보다 작거나 같은 5의 k승까지 체크해주면 된다.

시간복잡도는 아마 O(log_5(n))
'''

import sys
input = lambda : sys.stdin.readline().rstrip()


n = int(input())

def solve(n):
    res = 0
    group = n // 5
    m = 5
    pos = n % m + 1
    p = 1
    n0 = n
    while group >= 1:
        res += (5**p)*(group*(group-1)//2) + pos*group
        p += 1
        m *= 5
        n //= 5
        pos = n0 % m + 1
        group = n // 5
        
    return res
    

print(solve(n))