def transform_to_sets(input_list):
    result_set = set()
    num_count = {}

    for num in input_list:
        if num not in num_count:
            num_count[num] = 1
            result_set.add(num)
        else:
            num_count[num] += 1
            result_set.add(str(num) * num_count[num])

    return result_set


list1 = [1, 1, 3, 3, 1]
list2 = [5, 5, 5, 5, 5, 5, 5]
list3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

res1 = transform_to_sets(list1)
res2 = transform_to_sets(list2)
res3 = transform_to_sets(list3)

print(res1)
print(res2)
print(res3)
