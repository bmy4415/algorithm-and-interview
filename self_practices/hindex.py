# find h-index when given citations array


# O(nlogn) time algorithm
def get_hindex_nlogn(citations):
    arr = citations[:] # to avoid inplace
    arr.sort()
    N = len(arr)
    for i in range(N):
        if arr[i] >= N-i:
            return N-i

    return 0


# O(n) time algorithm
def get_hindex_n(citations):
    N = len(citations)
    bucket = [0] * (N+1)
    for c in citations:
        bucket[min(N, c)] += 1

    accumulated = 0
    for i in reversed(range(N+1)):
        accumulated += bucket[i]
        if accumulated >= i:
            return i


test_cases = [
    [3, 0, 6, 1, 5], # 3
    [1, 1, 1, 1, 1], # 1
    [5, 5, 5, 5], # 4
    [1, 2, 3, 4, 5], # 3
    [5, 4, 1, 3, 2], # 3
    [22, 42], # 2
    [5], # 1
    [1, 3, 5, 7, 9], # 3
    [4, 4, 0, 0], # 2
    [0, 0], # 0
    [], # 0
]

for t in test_cases:
    # print(t, '->', get_hindex_nlogn(t))
    print(t, '->', get_hindex_n(t))

