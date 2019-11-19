'''
Problem URL: https://www.acmicpc.net/problem/10866
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
    deq = deque()
    for _ in range(N):
        command, *args = sys.stdin.readline().strip().split()
        if command == 'push_front':
            deq.append(args[0])
        elif command == 'push_back':
            deq.appendleft(args[0])
        elif command == 'pop_front':
            print(-1 if len(deq) == 0 else deq.pop())
        elif command == 'pop_back':
            print(-1 if len(deq) == 0 else deq.popleft())
        elif command == 'size':
            print(len(deq))
        elif command == 'empty':
            print(1 if len(deq) == 0 else 0)
        elif command == 'front':
            print(-1 if len(deq) == 0 else deq[-1])
        elif command == 'back':
            print(-1 if len(deq) == 0 else deq[0])
