class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        localmin = prices[0]
        for i in range(len(prices)):
            if prices[i] > localmin:
                maxprofit += prices[i] - localmin
            localmin = prices[i]
        return maxprofit