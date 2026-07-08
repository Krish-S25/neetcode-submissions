class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td = {}
        if(s == "" or t == ""):
            return ""

        for j in t:         #make a frequency map for how many characters are needed for t
            if j not in td: #i.e. in td, td['p'] = 1 meens we need one p
                td[j] = 0   #also td['p'] = -1 shows we have 1 extra p
            td[j]+=1

        n = len(s)
        smallest = float("inf")  # min length for smallest window
        finalL = 0  # shows the starting L for smallest window
        R = 0
        L = 0
        count = len(td)    # keeps count of how many unique elements are needed in window

        while (R < n): 
            ch = s[R]       # Start expanding window with R 
            if ch in td:    
                td[ch]-=1
                if td[ch] == 0:  # Fully satisfied 1 unique element of td
                    count-=1
            R+=1                 # Move to next R and focus on shrinking window with L
            while count == 0 :
                if R-L < smallest:  # New smallest window found
                    smallest = R-L  # Noted length
                    finalL = L      # Noted start
                ch = s[L]          
                if ch in td:        # Handling the removal of a unique character we need
                    td[ch] += 1
                    if td[ch] > 0 :
                        count += 1
                L+=1                # Moves forward
            
        if smallest == float("inf") : 
            return ""
        else:
            return s[finalL : finalL + smallest]  #smallest window
