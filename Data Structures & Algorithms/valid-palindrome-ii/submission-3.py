class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0     #Optimal approach
        r = len(s)-1
    
        while l<r:
            if s[l]!=s[r]:
                lskip = s[l+1: r+1]    #takes middle part l+1 to r  , ignores l
                rskip = s[l:r]         #takes middle part l to r-1  , ignores r
                return (lskip == lskip[::-1]) or (rskip == rskip[::-1])
            l+=1
            r-=1
        return True
        