class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "": 
            return ""

        def findMax(left, right):
            while (left>=0 and right<=len(s)-1 and s[left] == s[right]):
                left-=1
                right+=1

            return right - left - 1
        start = 0
        longest = 0
        size = len(s)

        for i in range(size):
            lenOdd = findMax(i, i)
            lenEven = findMax(i, i+1)
            current_longest = max(lenOdd, lenEven)

            if current_longest > longest:
                longest = current_longest
                start = i - (current_longest-1)//2

        return s[start : start + longest ]

