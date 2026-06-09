class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sk = []
        for p in tokens:
            if p not in "+-*/":
                sk.append(p)
            else:
                o1 = int(sk.pop())
                o2 = int(sk.pop())
                match p:
                    case '+':
                        sk.append(o2 + o1)
                    case '-':
                        sk.append(o2 - o1)
                    case '*':
                        sk.append(o2 * o1)
                    case '/':
                        sk.append(o2/o1)

        return int(sk[0])

