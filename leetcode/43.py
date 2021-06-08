# https://leetcode.com/problems/multiply-strings/
# 43. Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res1 = 0
        res2 = 0
        mult = 1
        for i in num1[::-1]:
            res1 += (ord(i)-ord('0'))*mult
            mult *= 10
        mult = 1
        for i in num2[::-1]:
            res2 += (ord(i)-ord('0'))*mult
            mult *= 10
        
        res = res1*res2
        if res == 0:
            return '0'
        tmp = []
        while res:
            tmp.append(chr(res%10+ord('0')))
            res //= 10
        
        return ''.join(tmp[::-1])