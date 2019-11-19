'''
Problem URL: https://www.acmicpc.net/problem/9012
'''

import sys
import os

def isVPS(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return 'NO'
            else:
                stack.pop()

    if len(stack) != 0:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        data = sys.stdin.readline().strip()
        print(isVPS(data))
