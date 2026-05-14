class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = dict()
        mx = 0
        for j in nums:
            if j not in d1:
                d1[j] = 1
            else:
                d1[j] += 1
            if d1[j] > mx:
                mx = d1[j]
        bd = []
        for i in range(mx):
            bd += [[]]
        for j in d1:
            bd[d1[j] - 1].append(j)

        res = []
        while k > 0:
            while bd and bd[-1] == []:
                bd.pop()
            last = bd[-1].pop()
            res.append(last)
            k -= 1

        return res
