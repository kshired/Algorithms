# https://leetcode.com/problems/powx-n/
# 50. Pow(x,n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPow(x,abs(n))
        if n == 0:
            return 1
        elif n % 2:
            res = self.myPow(x,n//2)
            return res*res*x
        else:
            res = self.myPow(x,n//2)
            return res*res