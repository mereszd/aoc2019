string_array = []
on_going = True


def do_operation(index, temp_array):
    first = temp_array[index+1]
    second = temp_array[index+2]
    third = temp_array[index+3]
    if temp_array[index] == 1:
        temp_array[third] = temp_array[first] + temp_array[second]
    elif temp_array[index] == 2:
        temp_array[third] = temp_array[first] * temp_array[second]
    else:
        return False
    return True


with open("02_input.txt", "r") as f:
    for line in f:
        string_array = line.split(",")

process_array = [int(i) for i in string_array]

for index1 in range(0, 100):
    for index2 in range(0, 100):
        temp_array = process_array.copy()
        temp_array[1] = index1
        temp_array[2] = index2
        on_going = True
        start_index = 0
        while on_going:
            on_going = do_operation(start_index, temp_array)
            start_index += 4
        if temp_array[0] == 19690720:
            print("Found it, the 100*{}*{} is {}".format(temp_array[1], temp_array[2], 100*temp_array[1]+temp_array[2]))
            break
        # else:
        #     print("{} and {} produces {}".format(temp_array[1], temp_array[2], temp_array[0]))


