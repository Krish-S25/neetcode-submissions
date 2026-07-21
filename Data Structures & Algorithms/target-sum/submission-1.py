class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #1D DP optimal space complexity
        total_sum = sum(nums)
        n = len(nums)
        if abs(target) > total_sum or (total_sum - target)%2 == 1:
            return 0
        
        subset_target = (total_sum + target)//2

        dp = [0]*(subset_target + 1)
        dp[0] = 1 #Base case , also dp[0][j] will be 0

        for nm in nums: #Avoid using same number by using backwards loop 
            for j in range(subset_target, nm-1 , -1):
                dp[j] += dp[j - nm]

        return dp[subset_target]


