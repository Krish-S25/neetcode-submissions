class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        if coins == []: 
            return 0
        
        dp = [amount + 1] * (amount+1)  #Amount + 1 is used as inf here
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin :
                    dp[i] = min(dp[i-coin] + 1, dp[i])
                
        if dp[amount] != amount + 1: # Reached last dp[-1] with given coins
            return dp[-1]
        
        else:
            return -1



        