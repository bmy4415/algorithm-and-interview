'''
longest common substring of X, Y
use DP(dynamic programming)
table LCSuffix[i][j] means length of Longest Common Suffix of (X0~X(i-1)) and (Y0-(Yj-1))
Longest Common Substring's length is max(LCSuffix)
Longest Common Substring can be found by going from max length to 0 via diagonal move
return (length, string)
'''

def LCS(X, Y):
    # initialize LCSuffix table
    # pad 0 at start of each dimension to simplify code
    LCSuffix = []
    for idx in range(len(X)+1):
        LCSuffix.append([0 for x in range(len(Y)+1)])

    for idx in range(1, len(X)+1):
        for jdx in range(1, len(Y)+1):
            if X[idx-1] == Y[jdx-1]:
                LCSuffix[idx][jdx] = LCSuffix[idx-1][jdx-1] + 1
            else:
                LCSuffix[idx][jdx] = 0

    LCS_length = -1
    LCS_string = ''
    _idx = -1 # x index of max length
    for idx in range(1, len(X)+1):
        for jdx in range(1, len(Y)+1):
            if LCSuffix[idx][jdx] > LCS_length:
                LCS_length = LCSuffix[idx][jdx]
                _idx = idx

    while idx>=1:
        LCS_string = X[idx-1] + LCS_string
        idx -= 1

    return (LCS_length, LCS_string)

tests = [
    [('GeeksforGeeks', 'GeeksQuiz'), 5],
    [('abcdxyz', 'xyzabcd'), 4],
    [('zxabcdezy', 'yzabcdezx'), 6],
]

for test in tests:
    X, Y = test[0]
    ans = test[1]
    length, string = LCS(X, Y)
    print(X.rjust(15), Y.rjust(15), 'ans:', str(ans).rjust(3), 'result:', str(length).rjust(3), string.ljust(10))