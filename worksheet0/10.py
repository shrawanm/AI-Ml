def sum_nested(lst):

    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total

nested_list = [[1, 2], [3, [4, 5]], 6]
print(sum_nested(nested_list))