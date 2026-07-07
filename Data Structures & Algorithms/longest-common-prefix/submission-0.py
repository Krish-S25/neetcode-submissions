
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre =  strs[0]

        for s in strs[1 : ]:
            cnt = 0

            while cnt < len(pre) and cnt < len(s) and pre[cnt] == s[cnt]:
                cnt+=1
            
            pre = pre[:cnt]

            if pre == "":
                return pre

        return pre
