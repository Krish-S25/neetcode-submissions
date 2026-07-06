class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapL = []
        for n in nums:
            heapq.heappush(heapL, n)

            if len(heapL) > k:
                heapq.heappop(heapL)
            
        return heapq.heappop(heapL)
            
