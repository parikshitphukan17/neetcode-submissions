import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                n2 = stack.pop()
                n1 = stack.pop()
                a = 0
                if i == "+":
                    a= n1+n2
                elif i == "-":
                    a= n1-n2
                elif i == "*":
                    a= n1*n2
                elif i == "/":
                    a= int(float(n1)/n2)
                stack.append(a)
            else:
                stack.append(int(i))
        return stack[0]



        