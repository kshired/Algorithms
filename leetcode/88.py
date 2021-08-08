# https://leetcode.com/problems/merge-sorted-array/
# Merge Sorted Array

# simple solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m,m+n):
            nums1[i] = nums2[i-m]
        
        nums1.sort()


# linear time solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        k = m+n-1
        
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        
        if j >= 0:
            nums1[:k+1] = nums2[:j+1]