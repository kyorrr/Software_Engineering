def remove_tuple(input_tuple, element_to_remove):
    if element_to_remove in input_tuple:
        index = input_tuple.index(element_to_remove)
        return input_tuple[:index] + input_tuple[index+1:]
    else:
        return input_tuple

tuple1 = (1, 2, 3)
result1 = remove_tuple(tuple1, 1)
print(result1)

tuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
result2 = remove_tuple(tuple2, 3)
print(result2)

tuple3 = (2, 4, 6, 6, 4, 2)
result3 = remove_tuple(tuple3, 9)
print(result3)