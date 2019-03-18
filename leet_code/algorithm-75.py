# https://leetcode.com/problems/sort-colors/


class Solution:
    # 2-pass algorithm
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        # 1 pass
        for num in nums:
            count[num] += 1

        # 2 pass
        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0

            elif i < count[0] + count[1]:
                nums[i] = 1

            elif i < count[0] + count[1] + count[2]:
                nums[i] = 2

        return

test_cases = [
    [2,0,2,1,1,0],
]

s = Solution()
for t in test_cases:
    print(t, end='')
    s.sortColors(t)
    print('->', t)
