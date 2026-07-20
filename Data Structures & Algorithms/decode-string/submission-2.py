class Solution:
    def decodeString(self, s: str) -> str:
        stk = [] 
        iteration = ""
        curr_str = ""

        for tkn in s:
            if tkn in "1234567890":
                iteration += tkn
    
            elif tkn == "[":
                stk.append((curr_str, int(iteration)))

                curr_str = "" #Reset for new string
                iteration = ""
            
            elif tkn == "]":
                prev_str, repeat = stk.pop()
                curr_str = prev_str + (curr_str * repeat)

            else:
                curr_str += tkn
            
        return curr_str

            
            



        