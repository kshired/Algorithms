# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        dp = []
        min_val = prices[0]
        for idx,val in enumerate(prices):
            if idx == 0:
                dp.append(val)
            else:
                dp.append(val-min_val)
                min_val = min(val,min_val)
        res = max(dp[1:])
        
        return res if res > 0 else 0