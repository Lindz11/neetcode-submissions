class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10000
        profit = 0
        for price in prices: 
            if price < buy: 
                buy = price
                continue
            if price - buy > profit: 
                profit = price - buy
        
        return profit