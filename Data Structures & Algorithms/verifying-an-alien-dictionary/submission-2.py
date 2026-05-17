class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ct = 0
        ordermap = dict()
        for st in order:
            ordermap[st] = ct
            ct+=1
        for j in range(len(words)-1):       #time complexity O(All characters in words)
            w1, w2 = words[j], words[j + 1]   
            for k in range(min( len(w1), len(w2) )):
                if w1[k]!=w2[k]:
                    if ordermap[w1[k]]>ordermap[w2[k]]:
                        return False
                    
                    break
            else:
                if len(w1) > len(w2):
                    return False
                
        return True
