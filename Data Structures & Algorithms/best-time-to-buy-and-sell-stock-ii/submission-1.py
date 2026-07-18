class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==0:
            return 0

        hold = [0]*(n) #Max profit by holding a stock by EOD
        sell = [0]*(n) #Max profit by not holding stock by EOD

        hold[0] = -prices[0]
        sell[0] = 0
        last_max = prices[0]
        last_min = 10001

        for i in range(1, n):
            curr = prices[i]

            hold[i] = max( sell[i-1]-curr , hold[i-1] )
            sell[i] = max( hold[i-1]+curr , sell[i-1] )

        return sell[n-1]  # No point in buying or holding any stock till last day
        