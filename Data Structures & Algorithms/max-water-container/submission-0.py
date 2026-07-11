class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        max_water = 0
        while(L < R):
            W = R - L
            H = min(heights[L], heights[R])

            current_water = H * W  # width * height

            if current_water > max_water:
                max_water = current_water

            if heights[L] > heights[R]:
                R-=1
            
            else: 
                L+=1

        return max_water
