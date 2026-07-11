class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        def reverse_selective(start:int, end:int, num):
            while (start<end):
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
                
        reverse_selective(0, n-1, nums)
        reverse_selective(0, k-1, nums)  
        reverse_selective(k, n-1, nums)
        

        

        