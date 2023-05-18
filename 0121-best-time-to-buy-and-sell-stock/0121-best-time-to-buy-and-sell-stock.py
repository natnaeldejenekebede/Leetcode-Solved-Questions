class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minimum_price = prices[0]
        maximum_profit = 0
        
        for price in prices:
            if price < minimum_price:
                minimum_price = price
            elif price - minimum_price > maximum_profit:
                maximum_profit = price - minimum_price
        
        return maximum_profit