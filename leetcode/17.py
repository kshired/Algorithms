# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        let = ["","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        n = len(digits)
        
        res = ['']
        for i in digits:
            tmp = []
            for val in res:
                for l in let[int(i)-1]:
                    tmp.append(val+l)
            res = tmp
        return res
                