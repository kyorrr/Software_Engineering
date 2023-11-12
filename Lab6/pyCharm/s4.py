def find_employee_entry_exit(log, employee_id):
    if employee_id not in log:
        return ()

    start_index = log.index(employee_id)
    end_index = log[start_index + 1:].index(employee_id) + start_index + 1 if employee_id in log[start_index + 1:] else None

    if end_index is None:
        return log[start_index:]
    else:
        return log[start_index:end_index + 1]

log1 = (1, 2, 3)
employee_id1 = 8
result1 = find_employee_entry_exit(log1, employee_id1)
print(result1)

log2 = (1, 8, 3, 4, 8, 8, 9, 2)
employee_id2 = 8
result2 = find_employee_entry_exit(log2, employee_id2)
print(result2)

log3 = (1, 2, 8, 5, 1, 2, 9)
employee_id3 = 8
result3 = find_employee_entry_exit(log3, employee_id3)
print(result3)