# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Longest Substring Without Repeating Characters

'''
O(N^2)으로 푸는 방법도 있지만,
슬라이딩 윈도우를 이용하면 O(N)을 이용해 해결가능

string의 원소를 순회하면서 dict에 (val,idx)로 저장된 값을 이용해
left, right를 계속 update하고
maximum 값도 update해줌.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = {} # val -> idx
        res = 0
        for h, val in enumerate(s):
            if val in d and l <= d[val]:
                l = d[val] + 1
            else:
                res = max(res,h-l+1)
            d[val] = h
        return res

