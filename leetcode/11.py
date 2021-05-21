# https://leetcode.com/problems/container-with-most-water/
# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = []
        s,e = 0,len(height)-1
        while s < e:
            h = min(height[s],height[e])
            res.append((e-s)*h)
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return max(res)