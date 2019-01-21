# quick sort

def quick_sort(arr) :
    if len(arr) <= 1 :
        return

    else :
        _quick_sort(arr, 0, len(arr)-1)

def _quick_sort(arr, start, end) :
    if start >= end :
        return

    pivot_index = partition(arr, start, end)
    _quick_sort(arr, start, pivot_index-1)
    _quick_sort(arr, pivot_index+1, end)

# 중간 index를 pivot으로 설정
def partition(arr, start, end) :
    pivot = arr[(start+end)//2]

    left = start
    right = end
    while True :
        while left <= end :
            if arr[left] >= pivot :
                break
            else :
                left += 1

        while right >= start :
            if arr[right] < pivot :
                break
            else :
                right -= 1

        if left < right :
            # swap
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

        else :
            break

    return left

arr = [5,3,7,6,2,1,4]
quick_sort(arr)
print('result: ', arr)