'''
Problem URL: https://www.acmicpc.net/problem/1655
'''

import sys
import os
import bisect
import heapq

'''
heap version was about 10 times faster than binary search version
'''


def binary_search(N):
    # use binary search to insert new number into arr
    # arr is always sorted and with length of arr, we can find number in middle
    # time complexity is O(nlogn)
    arr = []
    for _ in range(N):
        curr = int(sys.stdin.readline().strip())
        bisect.insort_left(arr, curr)
        middle = (len(arr) - 1) // 2
        print(arr[middle])

def double_heap(N):
    # make minheap and maxheap such that
    # (max item of maxheap) <= (min item of minheap) and
    # len(maxheap) - len(minheap) <= 1
    # by doing this, middle number is always top of maxheap

    if N == 1:
        print(int(sys.stdin.readline().strip()))
        return

    first = int(sys.stdin.readline().strip())
    second = int(sys.stdin.readline().strip())
    print(first)
    big, small = max(first, second), min(first, second)
    print(small)
    maxheap, minheap = [(-small, small)], [big]   # use trick to use maxheap in python

    for _ in range(N - 2):
        curr = int(sys.stdin.readline().strip())
        if len(maxheap) == len(minheap):
            if curr <= minheap[0]:
                heapq.heappush(maxheap, (-curr, curr))
            else:
                min_top = heapq.heappop(minheap)
                heapq.heappush(maxheap, (-min_top, min_top))
                heapq.heappush(minheap, curr)
        else:
            max_top = maxheap[0][1]
            if curr < max_top:
                heapq.heappop(maxheap)
                heapq.heappush(minheap, max_top)
                heapq.heappush(maxheap, (-curr, curr))
            else:
                heapq.heappush(minheap, curr)

        print(maxheap[0][1])


if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N = int(sys.stdin.readline().strip())
    # binary_search(N)
    double_heap(N)
