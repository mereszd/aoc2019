def modify_list(process_array):
    process_array[4] = 999
    return True

process_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
modify_list(process_array)
print(process_array)