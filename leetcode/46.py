# https://leetcode.com/problems/permutations/
# 46. Permutations

from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums,len(nums)))