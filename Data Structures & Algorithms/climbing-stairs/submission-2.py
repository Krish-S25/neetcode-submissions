class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:     #optimal Bottoms up 
            return 1
        n_2 = 1
        n_1 = 1
        for i in range(1, n):
            temp = n_1
            n_1 = n_2 + n_1
            n_2 = temp
        
        return n_1