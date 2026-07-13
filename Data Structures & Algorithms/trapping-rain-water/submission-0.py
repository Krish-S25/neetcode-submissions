class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0 
        R = len(height) - 1

        left_max = height[L]
        right_max = height[R]

        total_water = 0

        while L<R :
            if left_max < right_max :
                L+=1 
                if height[L] > left_max:
                    left_max = height[L]

                total_water += left_max - height[L]     

            else :
                R-=1 
                if height[R] > right_max:
                    right_max = height[R]

                total_water += right_max - height[R]     

        return total_water