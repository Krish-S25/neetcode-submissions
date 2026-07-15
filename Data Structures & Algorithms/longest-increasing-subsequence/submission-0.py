class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
# dp[i] = longest increasing subsequence in nums[0...i] including i
        n = len(nums)
        dp = [1] * (n+1)
        dp[0] = 1

        for i in range(1, n):
            for j in range(i-1 , -1 , -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
        return max(dp)
            
                
            
        
