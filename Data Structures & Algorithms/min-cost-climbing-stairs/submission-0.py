class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * n
                            #TOP DOWN DP w/ MEMOIZATION
        def dp(i):
            if i == 0 or i == 1 :
                return cost[i]
            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(dp(i-1), dp(i-2))

            return memo[i]

        return min(dp(n-1),dp(n-2))



