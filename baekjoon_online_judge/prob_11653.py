'''
Problem URL: https://www.acmicpc.net/problem/11653
'''

import sys
import os
import math

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N = int(sys.stdin.readline().strip())
    factors = []
    while True:
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                factors.append(i)
                N //= i
                break

        # for-else statement in python
        # else if evaluated when for-loop is end normally, which is, break is not done
        else:
            if N != 1:
                factors.append(N)
            break # break while loop

    for f in factors:
        print(f)