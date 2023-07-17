# 3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = ""
s5 = " "
s6 = "a"
s7 = "aa"
s8 = "dvdf"

class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        substring_len_lst = []
        i = 0
        while i < len(s):
            substring_len = 0
            lookup = dict()
            k = i
            while k < len(s):
                char = s[k]
                if lookup.get(char, 0) == 1:
                    if substring_len == 0:
                        substring_len += 1
                    substring_len_lst.append(substring_len)
                    break
                lookup[char] = 1
                substring_len += 1
                k += 1
            i = k
        try:
            return max(substring_len_lst)
        except:
            return 0



# solution = Solution()
# print(solution.lengthOfLongestSubstring(s1))
# print(solution.lengthOfLongestSubstring(s2))
# print(solution.lengthOfLongestSubstring(s3))
# print(solution.lengthOfLongestSubstring(s4))
# print(solution.lengthOfLongestSubstring(s5))
# print(solution.lengthOfLongestSubstring(s6))
# print(solution.lengthOfLongestSubstring(s7))


class Solution2:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        substring_len_lst = []
        i = 0
        substring_len = 0
        lookup = dict()
        while i < len(s):
            char = s[i]
            if lookup.get(char, 0) == 1:
                substring_len_lst.append(substring_len)
                substring_len = 0
                lookup.clear()
                continue
            lookup[char] = 1
            substring_len += 1
            i += 1
        substring_len_lst.append(substring_len)
        return max(substring_len_lst)

# solution = Solution2()
# print(solution.lengthOfLongestSubstring(s1))
# print(solution.lengthOfLongestSubstring(s2))
# print(solution.lengthOfLongestSubstring(s3))
# print(solution.lengthOfLongestSubstring(s4))
# print(solution.lengthOfLongestSubstring(s5))
# print(solution.lengthOfLongestSubstring(s6))
# print(solution.lengthOfLongestSubstring(s7))
# print(solution.lengthOfLongestSubstring(s8))

class Solution3:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        longest = 0
        sub_count = 0
        l, r = 0, 0
        while r < len(s):
            substring = s[l:r+1]
            char = s[r]
            if char in substring[:-1]:
                l = substring.find(char) + 1 + l
                if sub_count > longest:
                    longest = sub_count
                sub_count = r - l
                continue
            sub_count += 1
            r += 1
        if sub_count > longest:
            longest = sub_count
        return longest

solution = Solution3()
print(solution.lengthOfLongestSubstring(s1))
print(solution.lengthOfLongestSubstring(s2))
print(solution.lengthOfLongestSubstring(s3))
print(solution.lengthOfLongestSubstring(s4))
print(solution.lengthOfLongestSubstring(s5))
print(solution.lengthOfLongestSubstring(s6))
print(solution.lengthOfLongestSubstring(s7))
print(solution.lengthOfLongestSubstring(s8))