class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        # Input: nums = [2,4,10,1,5], k = 2
        # cumulative = [2, 6, 16, 17, 5] ,total sum = 22
        #Mid = 11 => find closest possible cumulative sum to 11

        def check_possible(split_limit : int) -> bool:
            subarrays = 1   #starting value
            current_sum = 0 

            for it in nums:
                current_sum += it
                if current_sum > split_limit:
                    current_sum = it
                    subarrays += 1
            
            return subarrays <= k  #if possible to get k subarrays

        L = max(nums)
        R = sum(nums)
        res = R

        while (L<=R):
            Mid = (R+L)//2
            if check_possible(Mid):
                R = Mid-1
                res = Mid
            else:
                L = Mid+1
        
        return res
                
            

