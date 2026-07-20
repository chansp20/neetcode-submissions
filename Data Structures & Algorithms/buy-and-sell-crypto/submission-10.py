class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price = prices[0]
        profit = 0
        max_price = []
        if len(prices)==1:
            return 0
        for i in range(1,len(prices)):
            if prices[i]<cheapest_price:
                cheapest_price = prices[i]
                profit = prices[i] - cheapest_price
                
            else:
                profit =  prices[i] - cheapest_price
            max_price.append(profit)
        return max(max_price)
            