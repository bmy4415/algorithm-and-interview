'''
Problem URL: https://www.acmicpc.net/problem/11286
'''

import sys
import os
import heapq

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N = int(sys.stdin.readline().strip())
    # when compare tuples, former element gets priority
    # so we can save value as (absolute value, real value)
    minheap = []    # element: (absolute value, real value)
    for _ in range(N):
        curr = int(sys.stdin.readline().strip())
        if curr == 0:
            # pop and print element
            print(0) if len(minheap) == 0 else print(heapq.heappop(minheap)[1])
        else:
            # push element
            heapq.heappush(minheap, (abs(curr), curr))
