class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            try:
                numeric = int(token)
                stack.append(numeric)
            except ValueError:
                if token == '+':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first + second))
                if token == '-':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first - second))
                if token == '/':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first / second))
                if token == '*':
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first * second))
        return stack.pop()
    
token1 = ["2","1","+","3","*"]
token2 = ["4","13","5","/","+"]
token3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

soln = Solution()
print(soln.evalRPN(token1))
print(soln.evalRPN(token2))
print(soln.evalRPN(token3))
            