def remove_element(lst, elem):

    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(remove_element(item, elem))
        elif item != elem:
            result.append(item)
    return result

nested_list = [[1, 2], [3, 2], [4, 5]]
print(remove_element(nested_list, 2))