class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sk = []
        for p in tokens:
            if p not in "+-*/":
                sk.append(int(p))
            else:
                o1 = sk.pop()
                o2 = sk.pop()
                match p:
                    case '+':
                        sk.append(o2 + o1)
                    case '-':
                        sk.append(o2 - o1)
                    case '*':
                        sk.append(o2 * o1)
                    case '/':
                        sk.append(int(o2 / o1))

        return sk[0]

