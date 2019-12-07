'''
Problem URL: https://www.acmicpc.net/problem/2609
'''

import sys
import os

def get_gcd(N, M):
    gcd = 1
    while N >= 2 and M >= 2:
        for i in range(2, min(N, M) + 1):
            if N % i == 0 and M % i == 0:
                gcd *= i
                N //= i
                M //= i
                break

        # python for-else statement
        # if for-loop is eneded without break statement, go into else statement
        else:
            break

    return gcd


if __name__ == '__main__':
    # freopen equivalent
    inputfile_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'input.txt')
    sys.stdin = open(inputfile_path, 'r')

    N, M = [int(x) for x in sys.stdin.readline().strip().split()]

    # N = GCD(N, M) * a, M = GCD(N, M) * b when a and b is coprime with each other
    gcd = get_gcd(N, M)
    lcm = gcd * (N // gcd) * (M // gcd)
    print(gcd)
    print(lcm)
