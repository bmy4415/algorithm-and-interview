'''
Problem URL: <problem url>
'''

import sys
import os
from functools import reduce

# return num!
def factorial(num):
    if num == 0:
        return 1
    return reduce(lambda x, y: x * y, range(1, num+1))

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N, K = [int(x) for x in sys.stdin.readline().strip().split()]
    answer = factorial(N) // factorial(K) // factorial(N - K)
    print(answer)