nums1, tgt1 = [2,7,11,15], 9
nums2, tgt2 = [2,3,4], 6
nums3, tgt3 = [-1,0], -1

class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left != right:
            combination = numbers[left] + numbers[right]
            if combination == target:
                return [left + 1, right + 1]
            elif combination > target:
                right -= 1
            elif combination < target:
                left += 1
        return None
        

solution = Solution()
print(solution.twoSum(nums1, tgt1))
print(solution.twoSum(nums2, tgt2))
print(solution.twoSum(nums3, tgt3))