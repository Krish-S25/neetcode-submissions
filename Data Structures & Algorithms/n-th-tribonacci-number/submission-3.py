class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n==1 or n==2 :
            return 1
        t_0 = 0
        t_1 = 1
        t_2 = 1 
        for n in range(2, n):
            t_0, t_1, t_2 = t_1, t_2, t_1 + t_2 + t_0   #python smart swap

        return t_2