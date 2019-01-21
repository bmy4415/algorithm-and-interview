'''
longest common subsequence of X, Y
use DP(dynamic programming)
table LCSubsequence[i][j] means length of Longest Common Subsequence of (X0~X(i-1)) and (Y0~(Yj-1))
Longest Common Subsequence's length is LCSubsequence[len(X)][len(Y)]
Longest Common Subsequences can be found by going from right down element(LCSubsequence[len(X)][len(Y)]) to left up
There can be many LCSs which is max length
return (length, list of LCSs)
'''
def LCS(X, Y):
    # initialize LCSubsequence table
    LCSubsequence = []
    for idx in range(len(X)+1):
        LCSubsequence.append([0 for x in range(len(Y)+1)])

    for idx in range(1, len(X)+1):
        for jdx in range(1, len(Y)+1):
            if X[idx-1] == Y[jdx-1]:
                LCSubsequence[idx][jdx] = LCSubsequence[idx-1][jdx-1] + 1
            else:
                sub1 = LCSubsequence[idx][jdx-1]
                sub2 = LCSubsequence[idx-1][jdx]
                LCSubsequence[idx][jdx] = max(sub1, sub2)

    LCS_length = LCSubsequence[len(X)][len(Y)]

    # get all LCSs
    # there can be duplicate string so use set
    def _LCS(table, idx, jdx):
        if table[idx][jdx] == 0:
            return {''}

        if X[idx-1] == Y[jdx-1]:
            return set(map(lambda x: x+X[idx-1], _LCS(table, idx-1, jdx-1)))

        # if left and top value are same, follow both
        if table[idx-1][jdx] == table[idx][jdx-1]:
            return set.union(_LCS(table, idx-1, jdx), _LCS(table, idx, jdx-1))

        # follow the bigger value
        if table[idx-1][jdx] > table[idx][jdx-1]:
            return _LCS(table, idx-1, jdx)
        else:
            return _LCS(table, idx, jdx-1)

    # print('table below')
    # for row in LCSubsequence:
    #     print(row)

    LCS_strings = _LCS(LCSubsequence, len(X), len(Y))

    return (LCS_length, LCS_strings)


tests = [
    [('ABCDGH', 'AEDFHR'), 3, 'ADH'],
    [('AGGTAB', 'GXTXAYB'), 4, 'GTAB'],
    [('ABCBDAB', 'BDCABA'), 4, 'BCAB']
]

for test in tests:
    X, Y = test[0]
    length = test[1]
    string = test[2]
    result_l, result_s = LCS(X, Y)
    print(X.rjust(10), Y.rjust(10), 'ans:', str(length).rjust(2), 'result:', str(result_l).rjust(2), result_s)
