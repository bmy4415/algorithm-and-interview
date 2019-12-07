'''
Problem URL: https://www.acmicpc.net/problem/1037
'''

import sys
import os

'''
answer is multiple of least factor and greatest factor
'''

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N = int(sys.stdin.readline().strip())
    factors = [int(x) for x in sys.stdin.readline().strip().split()]
    factors.sort()
    print(factors[0] * factors[-1])
