# in-place quick sort

def quick_sort(arr, start, end):
    # print('start, end', start, end)
    if start >= end:
        return

    pivot = arr[start]
    left = [x for x in arr[start+1:end] if x<=pivot] # pivot 자신은 제외
    right = [x for x in arr[start:end] if x>pivot]
    # print('left, right', left, right)
    arr[start:end] = left + [pivot] + right
    quick_sort(arr, start, start+len(left))
    quick_sort(arr, start+len(left)+1, end)


test_cases = [
    [1,1,1],
    [1,2,3],
    [3,2,1],
    [1,3,2,2]
]

for t in test_cases:
    print(t, '->', end='')
    quick_sort(t, 0, len(t))
    print(t)
