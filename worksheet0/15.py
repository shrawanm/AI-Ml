def average_nested(lst):

    total_sum = sum_nested(lst)
    flat_list = deep_flatten(lst)
    return total_sum / len(flat_list) if flat_list else 0

nested_list = [[1, 2], [3, 4], [5, 6]]
print(average_nested(nested_list))