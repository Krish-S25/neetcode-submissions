class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        L = 0
        R = 0
        n = len(nums)
        window = set()
        
        while R < n:
            # If our current window footprint expands beyond k elements
            if R - L > k:
                window.remove(nums[L])
                L += 1
                
            # Perform instant O(1) duplicate check
            if nums[R] in window:
                return True
                
            # If unique, add it to our tracking hash set and expand the right bound
            window.add(nums[R])
            R += 1
            
        return False