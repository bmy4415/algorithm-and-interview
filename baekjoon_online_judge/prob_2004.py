'''
Problem URL: https://www.acmicpc.net/problem/2004
'''

import sys
import os
import math

# nCr = n! / (n-r)! / r!
# counting occurence of 5s in n! is logn
# time complexity = O(logn)
def solution(n, m):
    # count occurence of 2s and 5s in (num!)
    def count(num, base):
        if num == 0:
            return 0
        result = 0
        end = int(math.log(num, base))
        for i in range(1, end + 1):
            result += num // (base ** i)
        return result

    # caution: need to count both 2 and 5
    # normarlly 2 appears more than 5 but in case of 6C2 which is 15
    # 5 appears more than 2
    # so we must count both 2 and 5
    twos = count(n, 2) - count(n - m, 2) - count(m, 2)
    fives = count(n, 5) - count(n - m, 5) - count(m, 5)
    answer = min(twos, fives)
    answer = max(answer, 0)
    return answer

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    n, m = [int(x) for x in sys.stdin.readline().strip().split()]
    m = min(m, n-m) # nCm = nC(n-m)
    answer = solution(n, m)
    print(answer)
