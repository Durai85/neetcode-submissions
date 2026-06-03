class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if len(stack) > 1:
                if t == '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                elif t == '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                elif t == '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                elif t == '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a/b))
                else:
                    stack.append(int(t))
            else:
                stack.append(int(t))

            print(stack)

        return stack[-1]