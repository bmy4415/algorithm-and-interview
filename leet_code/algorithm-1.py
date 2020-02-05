# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input has exactly 1 solution.
        Be careful not to use same index. Same value with different
        index is allowed. For example, answer of ([3 ,3], 6) is [0, 1].
        Answer of ([3, 2, 4], 6) is [1, 2].
        """

        dic = dict() # key: number in nums, value: index of number
        for (idx, num) in enumerate(nums):
            remain = target - num

            if remain in dic:
                return [dic[remain], idx]

            dic[num] = idx