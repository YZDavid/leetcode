# 704. Binary Search - https://leetcode.com/problems/binary-search/

num1, tar1 = [-1,0,3,5,9,12], 9
num2, tar2 = [-1,0,3,5,9,12], 2


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1

    
solution = Solution()
print(solution.search(num1, tar1))
print(solution.search(num2, tar2))