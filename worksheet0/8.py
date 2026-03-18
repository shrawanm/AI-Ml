def flatten(lst):
    flattened = []
    for sublist in lst:
        for item in sublist:
            flattened.append(item)
    return flattened
nested_list = [[2, 3], [4,5], [6]]
result = flatten(nested_list)
print(result)