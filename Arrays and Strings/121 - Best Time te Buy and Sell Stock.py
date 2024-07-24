class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        maxprofit = 0
        localmin = prices[0]
        for i in range(len(prices)):
            # CASE 1 - New maxprofit
            if prices[i] - localmin > maxprofit:
                maxprofit = prices[i] - localmin
            # CASE 2 - New localmin
            elif prices[i] < localmin:
                localmin = prices[i]
        return maxprofit