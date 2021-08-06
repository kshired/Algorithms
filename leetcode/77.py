# https://leetcode.com/problems/combinations/
# Combinations
class Solution:
    def combinations(arr,n):
        if n == 0:
            return [[]]
        
        res = []
        
        for i in range(len(arr)):
            now = arr[i]
            rest = arr[i+1:]
            for combination in combinations(rest,n-1):
                res.append([now]+combination)
        
        return res
            
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations([i for i in range(1,n+1)],k)
    