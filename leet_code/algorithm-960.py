# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        '''
        dp[i]는 A의 각 row의 subsequence 들에 대하여 row[i]로 끝나는 subsequence 중
        maximum length of lexicographical subsequence를 의미한다.
        dp[i+1]은 만약 모든 row에 대하여 row[i+1] >= row[k]이면 dp[k]+1, 아니면 skip이 된다.
        특히 dp[idx] = max(dp[idx], dp[jdx]+1)에서 max를 이용한 이유는, jdx가 0~idx까지 움직이는데, 만약 작은 jdx(예를들어 2)에서
        update한 dp[idx]가 큰 jdx(예를들어 5)에서 update하려고 할 때, 더 작은 값으로 update하면 안되므로, 기존에 (이미 변경되어 있을 수 있는)값
        과 비교하여 더 큰값을 이용한다
        
        dp[i]가 row[i]로 끝나는 subsequence(row[i]까지의 전체 subsequence 가 아닌)인 이유는, (i+1)번째 character와 비교하여 subsequence
        의 길이가 늘어나는지 확인하려면 max length일 때 가장 마지막 character가 무엇인지 알아야 하므로 단순히 row[i]의 subsequence 중의
        max length of lexico subsequcen를 사용하지 못하고 row[i]로 끝나는 subsequence 중에서 비교해야 한다
        '''

        N = len(A)
        M = len(A[0])
        dp = [1 for x in range(M)]

        for idx in range(1, len(dp)):
            for jdx in range(0, idx):
                if all([A[kdx][idx] >= A[kdx][jdx] for kdx in range(N)]):
                    dp[idx] = max(dp[idx], dp[jdx]+1)
        return M - max(dp)

s = Solution()

tests = [
    [["baabab"], 2],
    [["babca","bbazb"], 3],
    [["edcba"], 4],
    [["ghi","def","abc"], 0],
    [["cbbdabc"], 3]
]

for test in tests:
    print('ans:', str(test[1]).rjust(2), 'result:', str(s.minDeletionSize(test[0])).rjust(2))