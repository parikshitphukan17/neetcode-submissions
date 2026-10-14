class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                n2,n1 = stack.pop(),stack.pop()
                if t == "+":
                    stack.append(n1+n2)
                elif t == "-":
                    stack.append(n1-n2)
                elif t == "/":
                    stack.append(int(float(n1/n2)))
                else:
                    stack.append(n1*n2)
        return stack[0]




        

     