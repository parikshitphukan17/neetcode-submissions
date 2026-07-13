class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
                continue
            n2,n1 = stack.pop(),stack.pop()
            n = 0
            if i == "+":
                n = n1+n2
            elif i == "-":
                n = n1-n2
            elif i == "*":
                n = n1*n2
            elif i == "/":
                n = int(float(n1/n2))
            stack.append(n)
        return stack[0]


        