class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ind = [0]*(n+1)   #we need n but we dont want to use 0th index
        for tp in trust:
            f= tp[0]
            s= tp[1]
            ind[f]-=1  #guy who trusts
            ind[s]+=1  #guy who gets trusted
        
        tv = n-1       #number of trust votes needed by judge
        for j in range(len(ind)):
            if ind[j] == tv:   #for judge case
                return j

        return -1
