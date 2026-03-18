def count_occurrences(lst, elem):

    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_occurrences(item, elem)
        elif item == elem:
            count += 1
    return count

nested_list = [[1, 2], [2, 3], [2, 4]]
print(count_occurrences(nested_list, 2))