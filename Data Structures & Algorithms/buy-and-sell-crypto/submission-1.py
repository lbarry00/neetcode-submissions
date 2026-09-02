class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for sell in prices:
            if sell > buy:
                profit = max(sell - buy, profit)
            else:
                buy = sell
                
        return profit