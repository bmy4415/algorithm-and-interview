'''
Problem URL: https://www.acmicpc.net/problem/10828
'''

import sys
import os

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    stack = []
    N = int(sys.stdin.readline().strip())
    for _ in range(N):
        line = sys.stdin.readline().strip().split()
        if line[0] == 'push':
            stack.append(int(line[1]))
        elif line[0] == 'pop':
            print(-1 if len(stack) == 0 else stack.pop())
        elif line[0] == 'size':
            print(len(stack))
        elif line[0] == 'empty':
            print(1 if len(stack) == 0 else 0)
        elif line[0] == 'top':
            print(-1 if len(stack) == 0 else stack[-1])
