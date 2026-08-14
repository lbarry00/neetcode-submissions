class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]

        for sell in range(len(prices)):
            sell_price = prices[sell]
            if sell_price > buy_price:
                profit = max(profit, sell_price - buy_price)
            else:
                buy_price = sell_price

        return profit