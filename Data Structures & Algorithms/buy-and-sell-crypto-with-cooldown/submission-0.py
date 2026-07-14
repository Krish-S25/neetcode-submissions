class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        hold = [0] * n  # Maximum profit on day i by holding the stock
        free = [0] * n  # Maximum profit on day i while empty handed and free to transact
        sold = [0] * n  # Maximum profit on day i given you sold it today

        hold[0] = -prices[0]
        sold[0] = 0
        free[0] = 0

        for i in range(1,n):
            hold[i] = max( hold[i-1], free[i-1] - prices[i])
                #Keep holding stock OR Buy with last free price - today price
            sold[i] = hold[i-1] + prices[i]
                # take previous max hold price and add todays selling price
            free[i] = max( free[i-1], sold[i-1] ) 
                #No buy & rest today OR we are in cool down from selling yesterday

        
        return max(sold[n-1], free[n-1])





