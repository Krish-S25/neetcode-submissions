class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapL = []    #Much better run time optimization
        for n in nums:
            heapq.heappush(heapL, n)

            if len(heapL) > k:
                heapq.heappop(heapL)
            
        return heapq.heappop(heapL)
            
