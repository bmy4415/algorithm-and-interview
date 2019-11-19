'''
Problem URL: https://www.acmicpc.net/problem/1021
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

    N, M = [int(x) for x in sys.stdin.readline().strip().split()]
    positions = [int(x) for x in sys.stdin.readline().strip().split()]

    answer = 0
    deq = deque(range(1, N + 1))
    for pos in positions:
        # find index of given position
        index = deq.index(pos)

        # pop element
        if index == 0:
            deq.popleft()
            continue

        # check if right is near or left is near
        if index <= len(deq) // 2:
            # left is near
            answer += index
            for _ in range(index):
                deq.append(deq.popleft())   # rotate left
            deq.popleft()                   # remove
        else:
            # right is near
            answer += len(deq) - index
            for _ in range(len(deq) - index):
                deq.appendleft(deq.pop())   # rotate right
            deq.popleft()                   # remove

    print(answer)
