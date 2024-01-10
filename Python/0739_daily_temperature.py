class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output = [0] * len(temperatures)
        stack = []
        for index, temp in sorted(enumerate(temperatures), reverse=True):
            while stack and stack[-1][1] <= temp:
                stack.pop()
            if len(stack) != 0:
                output[index] = stack[-1][0] - index
            stack.append((index, temp))
        return output
            

temp1 = [73,74,75,71,69,72,76,73]
temp2 = [30,40,50,60]
temp3 = [30,60,90]

soln = Solution()
print(soln.dailyTemperatures(temp1))
print(soln.dailyTemperatures(temp2))
print(soln.dailyTemperatures(temp3))