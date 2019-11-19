'''
Problem URL: https://www.acmicpc.net/problem/2164
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

    N = int(sys.stdin.readline().strip())
    deq = deque(range(1, N + 1))
    while len(deq) > 1:
        deq.popleft()               # remove first element
        deq.append(deq.popleft())   # move second element to last

    print(deq[0])
