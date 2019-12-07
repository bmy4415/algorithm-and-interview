'''
Problem URL: https://www.acmicpc.net/problem/9375
'''

import sys
import os
from collections import defaultdict
from itertools import combinations
from functools import reduce

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        clothes_dict = defaultdict(lambda: 0)   # key: type, value: number of clothes
        N = int(sys.stdin.readline().strip())
        for _ in range(N):
            _, clothes_type = sys.stdin.readline().strip().split()
            clothes_dict[clothes_type] += 1

        # add 1 to add option that does not ware clothes
        # remove 1 to remove the case where no clothes are used
        answer = reduce(lambda x, y: x * y, [x + 1 for x in clothes_dict.values()], 1)
        answer -= 1
        print(answer)