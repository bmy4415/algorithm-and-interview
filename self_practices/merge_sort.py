def merge_sort(arr) :
    def merge(left, right) :
        l1 = len(left)
        l2 = len(right)
        result = [0] * (l1 + l2)
        i = 0 # left index
        j = 0 # right index
        k = 0 # result index

        while i < l1 and j < l2 :
            if left[i] < right[j] :
                result[k] = left[i]
                i += 1
                k += 1

            else :
                result[k] = right[j]
                j += 1
                k += 1

        if i == l1 :
            while j < l2 :
                result[k] = right[j]
                j += 1
                k += 1

        if j == l2 :
            while i < l1 :
                result[k] = left[i]
                i += 1
                k += 1

        return result

    if len(arr) > 1 :
        start = 0
        end = len(arr)
        mid = (start+end) // 2
        left = merge_sort(arr[start:mid])
        right = merge_sort(arr[mid:end])
        return merge(left, right)

    else :
        return arr



arr = [3,1,7,8,3,6,2]
print(arr)
print(merge_sort(arr))