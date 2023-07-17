# 153. Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

num1 = [3,4,5,1,2]
num2 = [4,5,6,7,0,1,2]
num3 = [11,13,15,17]
num4 = [2,1]
num5 = [3]
num6 = [3,1,2]
num7 = [4,5,1,2,3]

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] > nums[r]:
            while l <= r: 
                m1 = (l + r) // 2
                m2 = m1 + 1
                if nums[m1] > nums[m2]:
                    return nums[m2]
                elif nums[m1] > nums[l]:
                    l = m1
                elif nums[m1] < nums[l]:
                    r = m1
        return nums[0]
    
solution = Solution()
print(solution.findMin(num1))
print(solution.findMin(num2))
print(solution.findMin(num3))
print(solution.findMin(num4))
print(solution.findMin(num5))
print(solution.findMin(num6))
print(solution.findMin(num7))