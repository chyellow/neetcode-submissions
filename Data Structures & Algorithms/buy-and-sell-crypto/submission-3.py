class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                result = max(result, profit)
            else:
                l = r
            r += 1
        
        return result