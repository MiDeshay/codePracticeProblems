import math

def my_b_search(arr, target):

    if len(arr) <= 0:
        return -1

    # pivot = int(math.floor(len(arr)/2))
    pivot = len(arr)//2

    left = arr[0 : pivot]
    right = arr[pivot+1 : ]


    if arr[pivot] == target:
        return pivot
    elif arr[pivot] > target:
       return my_b_search(left, target)
    else: 
        result = my_b_search(right, target)
        if(result != -1):
            return pivot + result + 1


l = [1,2,3,4,5,6,7,8]

print(my_b_search(l, 0))