# 238. Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/description/

num1 = [1,2,3,4]
num2 = [-1,1,0,-3,3]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        postfix = []
        running_product = 1
        for i in nums:
            running_product *= i
            prefix.append(running_product)
        running_product = 1
        for i in nums[::-1]:
            running_product *= i
            postfix.append(running_product)
        postfix = postfix[::-1]
        output = []
        for i in range(1, len(nums) - 1):
            product = prefix[i - 1] * postfix[i + 1]
            output.append(product)
        output.append(prefix[-2])
        output.insert(0, postfix[1])
        return output

    
solution = Solution()
print(solution.productExceptSelf(num1))
print(solution.productExceptSelf(num2))


### Rewrite after a week ###


class Solution2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l2r_prod = []
        r2l_prod = []
        output = []
        prod_value = 1
        for i in nums:
            prod_value *= i
            l2r_prod.append(prod_value)
        prod_value = 1
        for i in range(len(nums)-1, -1, -1):
            prod_value *= nums[i]
            r2l_prod.append(prod_value)
        r2l_prod = r2l_prod[::-1]

        for i in range(1, len(nums)-1):
            before_num = l2r_prod[i-1]
            after_num = r2l_prod[i+1]
            output.append(before_num * after_num)
        output.append(l2r_prod[-2])
        output.insert(0, r2l_prod[1])
        return output

            
solution = Solution2()
print(solution.productExceptSelf(num1))
print(solution.productExceptSelf(num2))