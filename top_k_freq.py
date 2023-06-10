nums1, k1 = [1,1,1,2,2,3], 2
nums2, k2 = [1], 1
nums3, k3 = [1,1,2,2,3], 2

class Solution:
    def topKFrequent(self, nums, k):
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        res = list(freq.items())
        res.sort(key=lambda x: (-x[1], x[0]))
        res = res[:k]
        return list(map(lambda x: x[0], res))
    
solution = Solution()
print(solution.topKFrequent(nums1, k1))
print(solution.topKFrequent(nums2, k2))
print(solution.topKFrequent(nums3, k3))

