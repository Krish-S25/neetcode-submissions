class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 1:
            return nums[0]
        def robHelper(arr: List[int]):
            n = len(arr)
            if n == 1:
                return arr[0]
            dp = [0]*n

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2,n):
                dp[i] = max(dp[i-1] , dp[i-2] + arr[i])
            
            return dp[-1]    #LAST ELEMENT

        return max(robHelper(nums[0 : L-1]) , robHelper(nums[1:L]) )
                    #       Includes 1st          Includes last



#    2,9,8,1,6,4,10,1,2,10

# dp[i] is the maximum we can get from 0 to ith house w/ i included
# dp[i] = max(dp[i-1] , dp[i-2] + nums[i])
# Base cases
# dp[0] = nums[0]
# dp[1] = max(nums[0],nums[1])