class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        n = len(tokens)
        for op in tokens:
            if op == "+":
                
                p = stack.pop()
                q = stack.pop()
                stack.append(p+q)
            elif op == "-":
                p = stack.pop()
                q = stack.pop()
                stack.append(q-p)
            elif op == "*":
                p = stack.pop()
                q = stack.pop()
                stack.append(p*q)
            elif op == "/":
                p = stack.pop()
                q = stack.pop()
                div = float(q)/p
                stack.append(int(div))

            else:
                stack.append(int(op))
                
        return stack[-1]
        