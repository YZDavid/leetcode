# 15. 3Sum - https://leetcode.com/problems/3sum/

test1 = [-1,0,1,2,-1,-4]
test2 = [0,1,1]
test3 = [0,0,0]
test4 = [0,0,0,0]

class Solution:
    def threeSum(self, nums):
        output = []
        nums.sort()
        i = 0
        prev = None
        while i < len(nums) - 2:
            first_num = nums[i]
            if first_num == prev:
                i += 1
                continue
            left, right = i + 1, len(nums) - 1
            left_prev = None
            while left != right:
                if nums[left] == left_prev:
                    left += 1
                    continue
                next_two = nums[left] + nums[right]
                if first_num + next_two == 0:
                    output.append([first_num, nums[left], nums[right]])
                    left_prev = nums[left]
                    left += 1
                elif next_two > -first_num:
                    right -= 1
                elif next_two < -first_num:
                    left_prev = nums[left]
                    left += 1
            i += 1
            prev = first_num
        return output
    
solution = Solution()
print(solution.threeSum(test1))
print(solution.threeSum(test2))
print(solution.threeSum(test3))
print(solution.threeSum(test4))