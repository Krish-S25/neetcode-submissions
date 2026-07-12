from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Fix 1: Initialize defaultdict properly with int
        d1 = defaultdict(int)
        for j in nums:
            d1[j] += 1
                
        # Simpler bucket strategy: array size is fixed to len(nums) + 1
        bd = [[] for _ in range(len(nums) + 1)]
        for num, freq in d1.items():
            bd[freq].append(num)

        res = []
        # Gather elements from the highest frequency down to 0
        for i in range(len(bd) - 1, 0, -1):
            for num in bd[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res