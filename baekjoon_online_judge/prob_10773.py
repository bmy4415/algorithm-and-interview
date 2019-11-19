'''
Problem URL: https://www.acmicpc.net/problem/10773
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
    K = int(sys.stdin.readline().strip())
    for _ in range(K):
        num = int(sys.stdin.readline().strip())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    print(sum(stack))
