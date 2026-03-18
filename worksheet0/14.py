def deep_flatten(lst):

    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(deep_flatten(item))
        else:
            flat_list.append(item)
    return flat_list

nested_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(deep_flatten(nested_list))