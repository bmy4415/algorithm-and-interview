'''
Problem URL: https://www.acmicpc.net/problem/17298
'''

import sys
import os

def solution(sequence):
    stack = []
    answer = [-1] * len(sequence)
    for i, num in enumerate(sequence):
        while stack and sequence[stack[-1]] < num:
            _i = stack.pop()
            answer[_i] = num  # write NGE

        stack.append(i)

    return ' '.join([str(x) for x in answer])

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N = int(sys.stdin.readline().strip())
    sequence = [int(x) for x in sys.stdin.readline().strip().split()]

    print(solution(sequence))
