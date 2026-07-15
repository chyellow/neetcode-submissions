class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        result = 0
        r = 1
        if len(prices) <= 1:
            return 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                result = max(profit, result)
            else:
                l = r
            r += 1

        return result
        