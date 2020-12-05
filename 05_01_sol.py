string_array = []
on_going = True

def check_opcode(start_index):
    opcode = str(process_array[start_index])
    params = [0, 0, 0]
    values = [0, 0, 0]
    on_going = True
    for i in range(3, len(opcode) + 1):
        params[i-3] = int(opcode[-i])
    increment = 0
    print("{} opcode and {} param codes.".format(opcode[-1], params))
    if opcode[-1] == '1':
        if params[0] == 0:
            values[0] = process_array[process_array[start_index+1]]
        else:
            values[0] = process_array[start_index + 1]
        if params[1] == 0:
            values[1] = process_array[process_array[start_index+2]]
        else:
            values[1] = process_array[start_index + 2]
        values[2] = values[0] + values[1]
        process_array[process_array[start_index + 3]] = values[2]
        print("Adding {} and {} up. Writing {} to position {}".format(values[0], values[1], values[2], process_array[process_array[start_index + 3]]))
        increment = 4
    elif opcode[-1] == '2':
        if params[0] == 0:
            values[0] = process_array[process_array[start_index + 1]]
        else:
            values[0] = process_array[start_index + 1]
        if params[1] == 0:
            values[1] = process_array[process_array[start_index + 2]]
        else:
            values[1] = process_array[start_index + 2]
        values[2] = values[0] * values[1]
        process_array[process_array[start_index + 3]] = values[2]
        print("Multiplying {} and {}. Writing {} to position {}".format(values[0], values[1], values[2], process_array[process_array[start_index + 3]]))
        increment = 4
    elif opcode[-1] == '3':
        user_input = int(input("Require input: "))
        process_array[process_array[start_index + 1]] = user_input
        print("Received input {}. Writing it to position {}".format(user_input, process_array[process_array[start_index + 1]]))
        increment = 2
    elif opcode[-1] == '4':
        print("Outputting the value at {}. Value: {}".format(process_array[start_index + 1], process_array[process_array[start_index + 1]]))
        increment = 2
    elif opcode[-1:-3:-1] == '99':
        print("Halt initiated.")
        on_going = False
    else:
        print("Unknown error, terminating")
        on_going = False
    return increment, on_going


with open("05_input.txt", "r") as f:
    for line in f:
        string_array = line.split(",")

process_array = [int(i) for i in string_array]

on_going = True
start_index = 0
input_char = 1

while on_going:
    increment, on_going = check_opcode(start_index)
    start_index += increment