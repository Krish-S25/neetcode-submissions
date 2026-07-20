class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = deque()
        res = ""
        items = path.split('/')

        for tkn in items:
            if tkn == "..":
                if stk:
                    stk.pop()
            #    //// case      /./.case
            elif tkn == "" or tkn == ".":
                continue
            
            else:                 #valid directory name
                stk.append(tkn)

        
        return "/" + "/".join(stk)

            
