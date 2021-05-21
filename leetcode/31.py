# https://leetcode.com/problems/next-permutation/
# 31. Next Permutation

class Solution:
    def next_permutation(self,arr):
        i = -1
        for idx in range(len(arr)-1):
            if arr[idx] < arr[idx+1]:
                i = max(i,idx)

        if i == -1:
            arr.sort()
            return
        
        j = i + 1
        for idx in range(i+1,len(arr)):
            if arr[idx] > arr[i]:
                j = max(idx,j)

        arr[i], arr[j] = arr[j], arr[i]

        arr[i+1:] = arr[len(arr):i:-1]


    def nextPermutation(self, nums: List[int]) -> None:
        self.next_permutation(nums)