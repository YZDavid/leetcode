class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        output = []
        stack = []

        def generate(left, right):
            if left == right == n:
                output.append(''.join(stack))
                return
            
            if left < n:
                stack.append("(")
                generate(left + 1, right)
                stack.pop()
            
            if right < left:
                stack.append(")")
                generate(left, right + 1)
                stack.pop()
            
            return

        generate(0, 0)
        return output
    
soln = Solution()
print(soln.generateParenthesis(3))
