# https://leetcode.com/problems/maximum-product-subarray/
# Maximum Product Subarray
'''
이건 어떻게 해야될지 모르겠어서.. 다른 사람의 풀이를 봤다.

maxVal은 양수의 곱을 저장
minVal은 음수의 곱을 저장

여기서 max, min을 적절히 사용하여 현재값부터 다시 시작하거나 최댓갑을 구함.

도대체 이런 풀이는 어떻게 생각하는걸까. 공부를 더하자
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = nums[0]
        minVal = nums[0]
        answer = nums[0]
        
        for i in range(1,len(nums)):
            now = nums[i]
            a = maxVal*now
            b = minVal*now
            maxVal = max(now, max(a,b))
            minVal = min(now, min(a,b))
            answer = max(answer,maxVal)
        
        return answer