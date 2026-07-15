class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        start_ind = 0
        n = len(s)  #EASY solution but suboptimal
        Memo = {}  #Time complexity O(n m t) len(s) ,len(wordDict) ,len(longest word)
        def recurse( start_ind : int):
            if start_ind == n:
                return True

            if start_ind in Memo:
                return Memo[start_ind]

            for word in wordDict:
                wlen = len(word)
                if s[start_ind : start_ind + wlen] == word:
                    if recurse( start_ind + wlen ):
                        Memo[start_ind] = True
                        return True
            
            Memo[start_ind] = False
            return False
        
        return recurse(0)

        