def get_sublist(lst, start, end):

    return lst[start:end+1]

numbers = [1, 2, 3, 4, 5, 6]
result = get_sublist(numbers, 2, 4)
print(result)