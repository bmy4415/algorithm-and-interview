'''
Problem URL: https://www.acmicpc.net/problem/2981
'''

import sys
import os
from functools import reduce
import math


# use euclidean algorithm
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a

def get_factors(num):
    factors = {num} # set
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            factors.update({i, num // i})

    return sorted(factors)

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N = int(sys.stdin.readline().strip())
    numbers = []
    for _ in range(N):
        numbers.append(int(sys.stdin.readline().strip()))

    diffs = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    largest_M = reduce(gcd, diffs)      # calculate GCD of all diffs
    answers = get_factors(largest_M)    # answer will be factors of GCD (except 1 and include GCD)
    print(' '.join([str(x) for x in answers]))
