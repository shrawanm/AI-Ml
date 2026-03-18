def find_max(lst):

    max_val = float('-inf')
    for item in lst:
        if isinstance(item, list):
            max_val = max(max_val, find_max(item))
        else:
            max_val = max(max_val, item)
    return max_val
\
nested_list = [[1, 2], [3, [4, 5]], 6]
print(find_max(nested_list))