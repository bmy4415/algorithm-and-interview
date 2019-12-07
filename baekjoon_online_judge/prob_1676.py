'''
Problem URL: https://www.acmicpc.net/problem/1676
'''

import sys
import os
import math

'''
2 must exist more times than 5
so we only need to check number of occurence of 5
time complexity: O(n)
'''
def solution(N):
    if N == 0:
        return 0

    fives = 0
    for i in range(1, int(math.log(N, 5)) + 1):
        if pow(5, i) <= N:
            fives += N // pow(5, i)

    return fives

'''
Since n! = n * (n-1) * ... 1, 5 must appear less than 2.
We need to count only occurence of 5
time complexity: O(logn)
'''
def solution_logn(N):
    # 0 must not be argument of math.log()
    if N == 0:
        return 0
    result = 0
    end = int(math.log(N, 5))
    for i in range(1, end + 1):
        result += N // (5 ** i)
    return result



if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N = int(sys.stdin.readline().strip())
    # print(solution(N))
    print(solution_logn(N))
