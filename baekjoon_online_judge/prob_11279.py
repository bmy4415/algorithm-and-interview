'''
Problem URL: https://www.acmicpc.net/problem/11279
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
    maxheap = []

    # heapq support only min heap
    # since input is positive, we can think of max heap by adding negative of input
    for _ in range(N):
        curr = int(sys.stdin.readline().strip())

        if curr == 0:
            # pop and print max element
            # elements in heap are negative now
            print(0 if len(maxheap) == 0 else -heapq.heappop(maxheap))
        else:
            # push
            heapq.heappush(maxheap, -curr)
