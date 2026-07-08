import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        slider = deque()
        n = len(nums)     #Fits O(n) solution AND IS MOST OPTIMAL
        result = []

        for i in range(n):
                     #Filter out all older out of range indices before i-k
            while slider and slider[0] <= i-k:
                slider.popleft()         #We maintain slider from i-k...i
                     #Filter out all indices of values smaller than nums[i] in i-k...i
            while slider and nums[slider[-1]] < nums[i]:
                slider.pop()             
            slider.append(i)

            if i >= k-1 :     #Now we have the largest latest valid item at 0th index
                result.append(nums[slider[0]])

        return result





            


