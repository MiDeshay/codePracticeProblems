def combinations(arr):
    if len(arr) == 0:
        return [[]]

    first = arr[0]
    rest = arr[1:]

    combsWithoutFirst = combinations(rest)
    print(combsWithoutFirst)
    combsWithFirst = []

    for comb in combsWithoutFirst:
        combWithFirst = comb + [first]
        combsWithFirst.append(combWithFirst)

    return combsWithoutFirst + combsWithFirst

print( combinations(['a', 'b', 'c']))



def my_combination(arr):
    if len(arr) == 1:
        return [[], [arr[0]]]
    
    first = arr[0]
    rest = my_combination(arr[1:])
    result = list(rest)

    for el in rest:
        result.append(el + [first])

    return result


print( my_combination(['a', 'b', 'c']))