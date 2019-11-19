'''
Problem URL: https://www.acmicpc.net/problem/1966
'''

import sys
import os
from collections import deque
import heapq

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        N, M = [int(x) for x in sys.stdin.readline().strip().split()]
        importance = [int(x) for x in sys.stdin.readline().strip().split()]

        # we need to save index in case of duplicate importance
        # deq[i] = (index, importance)
        deq = deque([(index, value) for (index, value) in enumerate(importance)])

        # store max elements
        # do not use set because I delete improtance from list
        # since list.pop() is O(1) and list.pop(i) is O(n), use ascending order list
        importance_list = sorted(importance)

        answer = 1
        while not(deq[0][0] == M and deq[0][1] == importance_list[-1]):
            front = deq.popleft()
            if front[1] < importance_list[-1]:
                deq.append(front)
            else:
                importance_list.pop()
                answer += 1

        print(answer)
