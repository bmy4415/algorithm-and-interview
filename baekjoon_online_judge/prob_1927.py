'''
Problem URL: https://www.acmicpc.net/problem/1927
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
    minheap = []

    for _ in range(N):
        curr = int(sys.stdin.readline().strip())

        if curr == 0:
            # pop and print min element
            print(0 if len(minheap) == 0 else heapq.heappop(minheap))
        else:
            # push
            heapq.heappush(minheap, curr)
