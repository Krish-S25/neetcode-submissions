class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #2D DP non optimal basic method
        total_sum = sum(nums)
        n = len(nums)
        if abs(target) > total_sum or (total_sum - target)%2 == 1:
            return 0
        
        subset_target = (total_sum + target)//2

        dp = [[0]*(subset_target + 1) for _ in range(n+1)]
        dp[0][0] = 1 #Base case , also dp[0][j] will be 0

        for i in range(1, n+1):
            n_i = nums[i-1]  

            for j in range(subset_target + 1) :
                dp[i][j] = dp[i-1][j] #Possible target sums before nums[i-1]
                   
                if j >= n_i:  #When [j-num] >= 0 and we can include nums[i-1]
                    dp[i][j] += dp[i-1][j - n_i]

        return dp[n][subset_target]


