import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        slider = []
        L = R = 0
        n = len(nums)
        result = []

        for i , num in enumerate(nums):
            heapq.heappush(slider, (-num,i))  
                        #-ve value for max heap and index to check for validity
            while slider[0][1] <= i-k:
                heapq.heappop(slider)

            if i >= k-1:     #Start saving after the first k elements
                result.append(-slider[0][0])
            
        return result





            


