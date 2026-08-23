class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=0
        m=0
        while r<len(prices):
            while r<len(prices) and prices[r]>prices[l]:
                r+=1
                m=max(m,prices[r-1]-prices[l])
            l=r
            r+=1
        return m