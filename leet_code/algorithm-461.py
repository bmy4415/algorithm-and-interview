# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        MAX_LEN = 31 # max bit length
        def decimal_to_binary_string(num):
            result = ['0'] * MAX_LEN
            i = MAX_LEN - 1
            while(num >= 2):
                q, r = divmod(num, 2)
                result[i] = str(r)
                num = q
                i -= 1

            result[i] = str(num)
            return ''.join(result)

        x_binary = decimal_to_binary_string(x)
        y_binary = decimal_to_binary_string(y)
        count = 0 # number of diffrent bits
        for i in range(MAX_LEN):
            if x_binary[i] != y_binary[i]:
                count += 1

        return count



s = Solution()
print(s.hammingDistance(1, 4))