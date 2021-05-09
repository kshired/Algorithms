# https://leetcode.com/problems/string-to-integer-atoi/
# 8. String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) < 1:
            return 0
        flag = False
        if s[0] == '-' or s[0] == '+':
            flag = True if s[0] == '-' else False
            s = s[1:]
        chk = len(s)
        for idx,val in enumerate(s):
            if not val.isdigit():
                chk = idx
                break
        s = s[:chk]
        try:
            s = int(s)
            if flag:
                s *= -1
        except:
            return 0
        maximum = 2**31
        if maximum*-1 <= s <= maximum-1:
            return s
        elif s > maximum-1:
            return maximum-1
        else:
            return maximum*-1