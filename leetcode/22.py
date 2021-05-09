# https://leetcode.com/problems/generate-parentheses/
# 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 1:
            return ["()"]
        res = []
        for j in self.generateParenthesis(n-1):
            res.append(j+"()")
            for idx,val in enumerate(j):
                if val == ")":
                    res.append(j[:idx]+"()"+j[idx:])
                
        return list(set(res))