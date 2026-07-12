class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        n = len(digits)
        numLetter ={"2": ("a", "b", "c"),"3": ("d", "e", "f"),
                    "4": ("g", "h", "i"),"5": ("j", "k", "l"),
                    "6": ("m", "n", "o"), "7": ("p", "q", "r", "s"),
                    "8": ("t", "u", "v"),"9": ("w", "x", "y", "z") }

        res = []

        def all_perms(ind, current_path):
            if ind == n :
                res.append("".join(current_path))
                return

            possible_letters = numLetter[digits[ind]]

            for k in possible_letters:
                current_path.append(k)
                all_perms(ind+1, current_path)
                current_path.pop()    #CLEAR last choice for new iteration

        all_perms(0, [])

        return res
