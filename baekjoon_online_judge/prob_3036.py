'''
Problem URL: https://www.acmicpc.net/problem/3036
'''

import sys
import os

# use euclidean algorithm to find gcd of 2 nubmers
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N = int(sys.stdin.readline().strip())
    radius = [int(x) for x in sys.stdin.readline().strip().split()]
    r0 = radius[0]
    answers = ['{}/{}'.format(r0 // gcd(r, r0), r // gcd(r, r0)) for r in radius[1:]]   # use gcd to find irreducible fraction
    for a in answers:
        print(a)