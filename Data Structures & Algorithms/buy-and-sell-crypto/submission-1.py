class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        m_profit = 0

        for price in prices:
            profit = price - min_price
            min_price = min(price, min_price)
            m_profit = max(profit, m_profit)

        return m_profit 
        
            

            
            

