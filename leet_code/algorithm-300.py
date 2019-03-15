# https://leetcode.com/problems/longest-increasing-subsequence/

'''
dp[i] = length of Longest Increasing Subsequence that has arr[i] as last element

nlogn 방법에서는 loop를 돌면서 가능한 LIS들 중에서 가장 작은 number만을 가지고 있도록 바꿔줌
대신 LIS가 실제 LIS sequence를 가지고 있지는 않고 가능한 조건만을 가지고 있는 상태
만약에 실제로 LIS sequence 자체가 필요하면 매 iteration 마다 update 해주는 position과 value를
저장하면 된다.
ex)
history = [[pos1, num1], [pos2, num2] ...] 형태로 저장한 후
history를 따라서 loop를 돌면서 구할 수 있음

'''


class Solution:
    # O(n^2) solution
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        # empty sequence
        if not nums:
            return 0

        N = len(nums)
        dp = [1] * N
        dp[0] = 1
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

        return max(dp)

    # O(nlogn) solution
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        import bisect

        # empty sequence
        if not nums:
            return 0

        LIS = []
        for num in nums:
            pos = bisect.bisect_left(LIS, num)
            if pos == len(LIS):
                LIS.append(num)
            else:
                LIS[pos] = num

        return len(LIS)



test_cases = [
    [4, 10, 4, 3, 8, 9],
    # [10,9,2,5,3,7,101,18],
]

s = Solution()
for t in test_cases:
    print(t, '->', s.lengthOfLIS(t))
