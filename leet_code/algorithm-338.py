# https://leetcode.com/problems/counting-bits/
'''
예시를 하나 살펴보면 num = 10일 때,
answer = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2] 이다
2진수는 잘 살펴보면 앞에서 반복되었던 패턴이 뒤에서 다시 반복 된다
0 = 0, 1 = 1
2 = 10, 3 = 11
4 = 100, 5 = 101, 6 = 110, 7 = 111
...
0,1의 숫자들이 2,3에서 맨 왼쪽 1bit을 제외하면 반복되고
0,1,2,3의 숫자들이 4,5,6,7에서 맨 왼쪽 1bit을 제외하면 반복된다
즉 2이상인 2의 거듭제곱인 i에 대해서, 0~(i-1)번 째의 2진수 패턴이 i~(2i-1)번 째의 숫자에 반복된다
이를 이용하면 O(num)의 시간복잡도에 원하는 답을 구할 수 있다
'''

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        # initialize arr
        arr = [0] * (num+1)
        arr[0] = 0

        i = 1
        while True:
            if i > num:
                return arr[:num+1]

            for j in range(i, min(2*i, num)+1):
                arr[j] = 1 + arr[j-i]

            i *= 2

s = Solution()
print(s.countBits(10))