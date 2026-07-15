class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for curr in range(1, target+1):
            for n in nums:
                if curr >= n:
                    dp[curr] += dp[curr-n]

        return dp[target]
            
