# https://leetcode.com/problems/divide-two-integers/
# 29. Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend/divisor)
        if res >= 2**31:
            return 2**31-1
        else:
            return res