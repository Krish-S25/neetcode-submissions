class Solution:

    def encode(self, strs: List[str]) -> str:
        new_word = ""
        for i, word in enumerate(strs):
            new_word += str(len(word)) + "$" + word
        
        return new_word
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while(i < len(s)):
            ch = s[i]
            j = i
            while (ch != "$"):
                j += 1
                ch = s[j]
    
            word_size = int(s[i:j])

            j+=1   #Start of the actual word
            word = s[j : j + word_size]

            res.append(word)
            i = j + word_size

        return res
            
                
            

        
