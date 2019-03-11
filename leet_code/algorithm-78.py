# https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        results = [[]]
        for i in range(len(nums)):
            item = nums[i]
            results += [x+[item] for x in results]

        return results



test_cases = [
    ([1,2,3], [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]])
]

s = Solution()
for t in test_cases:
    print(t[1], '<->', s.subsets(t[0]))
