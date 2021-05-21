# https://leetcode.com/problems/count-and-say/
# 38. Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        tmp = ""
        res = ""
        count = 0
        for i in self.countAndSay(n-1):
            if not tmp or tmp == i:
                count += 1
                tmp = i
            if tmp!= i:
                res += str(count)+tmp
                tmp = i
                count = 1
        if count:
            res += str(count)+tmp
        return res