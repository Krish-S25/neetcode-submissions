class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1] , dp[i-2] + nums[i])
        
        return dp[n-1]





#    2,9,8,1,6,4,10,1,2,10

# dp[i] is the maximum we can get from 0 to ith house w/ i included
# dp[i] = max(dp[i-1] , dp[i-2] + nums[i])
# Base cases
# dp[0] = nums[0]
# dp[1] = max(nums[0],nums[1])