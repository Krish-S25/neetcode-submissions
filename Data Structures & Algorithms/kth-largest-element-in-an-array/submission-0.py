import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)       # simplest way but not optimal 
        for i in range(len(nums)-k):  #stores way more elements in heap than needed
            heapq.heappop(nums)

        return heapq.heappop(nums)