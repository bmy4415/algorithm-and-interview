'''
Problem URL: https://www.acmicpc.net/problem/1874
'''

import sys
import os

def solution(n, sequence):
    stack = []
    command = [None] * 2 * n    # commands are at most 2n
    curr = 1

    for num in sequence:
        # push until num == curr then pop once
        if num > curr:
            stack.extend(range(curr, num))
            command.extend(['+'] * (num - curr +1) + ['-'])
            curr = num + 1

        # push and pop
        elif num == curr:
            command.extend(['+', '-'])
            curr += 1

        else:
            top = stack[-1] if len(stack) != 0 else None
            # top must be equal to num
            if top != num:
                sys.stdout.write('NO\n')
                return

            stack.pop()
            command.append('-')

    for op in [x for x in command if x is not None]:
        sys.stdout.write('{}\n'.format(op))

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    n = int(sys.stdin.readline().strip())
    sequence = [None] * n
    for i in range(n):
        sequence[i] = int(sys.stdin.readline().strip())

    solution(n, sequence)
