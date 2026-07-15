class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 :
            return 0
        
        abs_max = nums[0]

        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, n):
            curr = nums[i]
            temp_max = curr_max

            curr_max = max( curr_min*curr, temp_max*curr, curr ) # MAX all options
            curr_min = min( curr_min*curr, temp_max*curr, curr ) # MIN all options
            abs_max = max( curr_max, abs_max)

        return abs_max

