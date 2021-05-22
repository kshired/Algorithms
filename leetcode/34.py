# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 34. Find First and Last Position of Element in Sorted Array

from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums:
            return [-1,-1]
        l = bisect_left(nums,target)
        r = bisect_right(nums,target)-1
        if nums[l] != target:
            l = -1
        if nums[r] != target:
            r = -1
        
        return [l,r]