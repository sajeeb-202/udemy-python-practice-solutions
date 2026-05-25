def remove_duplicates(input_list):
    result = []

    for item in input_list:
        if item not in result:
            result.append(item)

    return result