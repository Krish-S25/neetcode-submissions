class Solution:
    def isValid(self, s: str) -> bool:
        l1=[]
        for k in s:
            if k in "{[(":
                l1.append(k)
                continue
            elif k in "]})":
                if l1==[]:
                    return False
                if k=="]" and l1[-1]=="[":
                    l1.pop()
                elif k==")" and l1[-1]=="(":
                    l1.pop()
                elif k=="}" and l1[-1]=="{":
                    l1.pop()
                else:
                    return False
        if l1!=[]:
            return False
        return True
        

        