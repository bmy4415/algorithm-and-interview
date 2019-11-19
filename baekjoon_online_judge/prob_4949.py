'''
Problem URL: https://www.acmicpc.net/problem/4949
'''

import sys
import os

def isBalanced(line):
    stack = []
    for char in line:
        if char not in ['(', ')', '[', ']']:
            continue

        if char in ['(', '[']:
            stack.append(char)

        elif char in [')', ']']:
            top = stack[-1] if len(stack) != 0 else None
            if (char == ')' and top != '(') or (char == ']' and top != '['):
                return 'no'

            # pop char's pair
            stack.pop()

    return 'yes' if len(stack) == 0 else 'no'

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    while True:
        line = sys.stdin.readline().rstrip('\n')
        if line == '.':
            break

        print(isBalanced(line))
