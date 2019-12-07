'''
Problem URL: https://www.acmicpc.net/problem/11051
'''

import sys
import os

'''
Combination has following property: nCr = (n-1)C(r-1) + (n-1)Cr
Since N <= 1000 and K <= N, maximum value of nCk is 1000C500 which is very very large.
In general programming language (C, C++, JAVA, ...), we cannot store this value in a variable like long.

We can use mod operation and above property since mod is open to addition.
For example, (A + B) % m == ((A % m) + (B % m)) % m.

Function "solution_dp" implements this.

But in python, integer is not bounded. It can have any integer. (I have tested 10^300 and it was fine)
So, we don't have to consider size of nCr.
This is implemented in function "solution_iter"

Time spent on each function is
solution_dp: 332ms
solution_iter: 56ms
'''

CACHE = dict()
MOD = 10007

# use property of combination and mod operation
def solution_dp(n, r):
    # base case
    if n == 1 or r == 0 or n == r:
        return 1

    # check cache
    if (n, r) in CACHE:
        return CACHE[(n, r)]

    result = (solution_dp(n - 1, r - 1) + solution_dp(n - 1, r)) % MOD
    CACHE[(n, r)] = result
    return result

# since python's int is unbounded, we can solve this naively
def solution_iter(n, r):
    result = 1
    for i in range(r):
        result = (result * (n - i)) // (i + 1)

    return result % MOD


if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N, K = [int(x) for x in sys.stdin.readline().strip().split()]
    k = min(K, N-K)     # nCk == nC(n-k), so use smaller one between (n, n-k)

    # answer = solution_dp(N, k)
    answer = solution_iter(N, k)
    print(answer)