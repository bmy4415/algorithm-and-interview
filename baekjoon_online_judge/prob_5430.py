'''
Problem URL: https://www.acmicpc.net/problem/5430
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

    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        p = sys.stdin.readline().strip()                    # command stirng
        n = int(sys.stdin.readline().strip())               # length of list
        splitted = sys.stdin.readline().strip()[1:-1].split(',')
        deq = deque(filter(None, splitted))                 # remove empty string('')

        # we don't have to reverse list
        # we can store if array should reversed

        is_reversed = 0    # 0: original, 1: reversed
        is_error = False
        for command in p:
            if command == 'R':
                is_reversed = 1 - is_reversed   # convert 0 to 1 and 1 to 0
            elif command == 'D':
                if len(deq) == 0:
                    is_error = True
                    break
                deq.pop() if is_reversed else deq.popleft()

        if is_error:
            print('error')
        else:
            if is_reversed:
                print('[{}]'.format(','.join(reversed(deq))))
            else:
                print('[{}]'.format(','.join(deq)))
