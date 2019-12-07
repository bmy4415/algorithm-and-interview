'''
Problem URL: https://www.acmicpc.net/problem/5086
'''

import sys
import os

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    while True:
        A, B = [int(x) for x in sys.stdin.readline().strip().split()]
        if (A, B) == (0, 0):
            break

        if B % A == 0:
            print('factor')
        elif A % B == 0:
            print('multiple')
        else:
            print('neither')

