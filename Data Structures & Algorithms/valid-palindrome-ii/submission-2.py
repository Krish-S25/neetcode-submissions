class Solution:
    def checkPal(self, s : str) -> bool:
        l = 0 
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        l = 0     #initial check goes through everything and finds all bad pairs
        r = len(s)-1
        issue = []
        while l<r:
            if s[l]!=s[r]:
                issue+=[l , r]
            l+=1
            r-=1
        if len(issue) == 0:                   #decent time complexity 
            return True                      #bad space complexity
        for k in range(len(issue)): 
            newst = s[0:issue[k]:] + s[issue[k]+1::]
            if self.checkPal(newst):
                return True
        return False
        