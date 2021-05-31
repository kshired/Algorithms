# https://leetcode.com/problems/sort-colors/
# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        self.quick_sort(nums,0,len(nums)-1)
    
    def quick_sort(self,arr,left,right):
        i = left
        j = right
        pivot = arr[(left+right)//2]
        
        while True:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
                j -= 1
            if i > j:
                break
                
        if left < j:
            self.quick_sort(arr,left,j)
        if i < right:
            self.quick_sort(arr,i,right)