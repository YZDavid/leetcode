test1 = ["eat","tea","tan","ate","nat","bat"]
test2 = [""]
test3 = ["a"]


class Solution1:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = dict()
        def letter_count(string):
            count = dict()
            for letter in string:
                try:
                    count[letter] += 1
                except:
                    count[letter] = 1
            return frozenset(count.items())
        for string in strs:
            key = letter_count(string)
            if key not in groups:
                groups[key] = []
            groups[key].append(string)
        return list(groups.values())

import collections
class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


    
solution = Solution1()
print(solution.groupAnagrams(test1))
print(solution.groupAnagrams(test2))
print(solution.groupAnagrams(test3))

solution = Solution2()
print(solution.groupAnagrams(test1))
print(solution.groupAnagrams(test2))
print(solution.groupAnagrams(test3))