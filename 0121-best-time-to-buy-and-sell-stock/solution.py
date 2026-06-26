class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=float('inf')
        max1=0
        for price in prices:
            min1=min(min1,price)
            max1=max(max1,price-min1)                    
        return max1        
