class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best_day = float("-inf")
        i = n - 1
        profit = 0
        while i >= 0:
            if prices[i] > best_day:
                best_day = prices[i]
            else:
                profit = max(profit, best_day - prices[i])
            i -= 1
        return profit 
