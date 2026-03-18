def access_nested_element(lst, indices):

    element = lst
    for index in indices:
        element = element[index]
    return element
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(access_nested_element(nested_list, [1, 2]))