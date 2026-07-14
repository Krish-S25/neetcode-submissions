class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        sum_by_2 = total_sum // 2

        dp = [False] * (sum_by_2 + 1)
        dp[0] = True

        for sn in stones:
            for wt in range(sum_by_2 , sn-1 , -1):
                if dp[wt - sn]:
                    dp[wt] = True
        
        for wt in range(sum_by_2, -1, -1):
            if dp[wt] :
                return total_sum - (2*wt)

        return 0
        