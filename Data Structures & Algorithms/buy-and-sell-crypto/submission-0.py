class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we want to buy at the lowest amount and sell at highest
        # each day represents a different price and each day is an increment of i
        # two pointer problem
        # left pointer is buy
        # right pointer is sell
        # how and why should we move the pointers

        # profit = 0
        # L = prices[0]
        # n = len(prices)
        # R = prices[n]

        l, r = 0, 1 # left and right pointer
        maxProfit = 0
        tmpProfit = 0
        while r < len(prices):
            # profitable? 
            if prices[l] < prices[r]:
                tmpProfit = prices[r] - prices[l]
                r += 1
                if maxProfit < tmpProfit:
                    maxProfit = tmpProfit
            elif prices[l] == prices[r]:
                r += 1
            else: # l > r
                l = r
                r += 1

        return maxProfit


        
