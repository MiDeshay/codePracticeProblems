def my_merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = int(len(arr)//2)

    sorted_left = my_merge_sort(arr[0:pivot])
    sorted_right = my_merge_sort(arr[pivot: ])

    return merge(sorted_left, sorted_right)

def merge(left, right):

    result = []

    while  left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    
    result += left
    result += right

    return result

my_list = [6,3,89,1,423,2,9,3]

print(my_merge_sort(my_list))