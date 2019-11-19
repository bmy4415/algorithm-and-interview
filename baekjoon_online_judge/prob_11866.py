'''
Problem URL: https://www.acmicpc.net/problem/11866
'''

import sys
import os
from collections import deque

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N, K = [int(x) for x in sys.stdin.readline().strip().split()]
    deq = deque(range(1, N + 1))
    result = [] # Josephus permutation
    while deq:
        # move first element to last (K-1) times
        for i in range(K - 1):
            deq.append(deq.popleft())

        result.append(deq.popleft())

    print('<{}>'.format(', '.join([str(x) for x in result])))
