class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = dict()
        nums_set = set(nums)
        # O(n)
        for num in nums_set:
            prev_num = num - 1
            # if no left neighbours, it is a start num
            if prev_num not in nums_set:
                longest[num] = 1
        
        # O(n)
        for start_num in longest:
            num = start_num
            while True:
                if num + 1 in nums_set:
                    longest[start_num] += 1
                    num += 1
                else:
                    break
        
        return max(longest.values())
            
soln = Solution()
print(soln.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    