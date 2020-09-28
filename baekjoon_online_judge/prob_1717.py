'''
Problem URL: <problem url>
'''

import sys
import os

# freopen equivalent
abs_path = os.path.abspath(__file__)
abs_path = os.path.join(os.path.dirname(abs_path), 'input.txt')
sys.stdin = open(abs_path, 'r')

if __name__ == '__main__':
