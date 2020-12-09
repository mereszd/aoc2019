def rw_to_program(process_array, position, value=False):
    if position < 0:
        print("Error, trying to write to negative position")
        return False
    longer = position-len(process_array)
    if longer >= 0:
        for i in range(longer+1):
            process_array.append(0)
    if value is False:
        return process_array[position]
    else:
        process_array[position] = value
    return value


def run_program(process_array, input_signal):
    # print("{} starting.".format(name))
    current_index = 0
    on_going = True
    jump = False
    increment = 0
    relative_base = 0
    while on_going:
        if jump:
            current_index = increment
            jump = False
        else:
            current_index += increment
        opcode = str(rw_to_program(process_array, current_index))
        params = [0, 0, 0]
        values = [0, 0, 0]
        # Setting up the parameters
        for i in range(3, len(opcode) + 1):
            params[i - 3] = int(opcode[-i])
        # Assigning position based on first param
        if params[0] == 0:
            pos = rw_to_program(process_array, current_index + 1)
        elif params[0] == 1:
            pos = current_index + 1
        elif params[0] == 2:
            pos = rw_to_program(process_array, current_index + 1) + relative_base
        values[0] = rw_to_program(process_array, pos)
        # Assigning position based on second param
        if params[1] == 0:
            pos = rw_to_program(process_array, current_index + 2)
        elif params[1] == 1:
            pos = current_index + 2
        elif params[1] == 2:
            pos = rw_to_program(process_array, current_index + 2) + relative_base
        values[1] = rw_to_program(process_array, pos)
        # Add
        if opcode[-1] == '1':
            values[2] = values[0] + values[1]
            if params[2] == 0:
                pos = rw_to_program(process_array, current_index + 3)
            elif params[2] == 2:
                pos = rw_to_program(process_array, current_index + 3) + relative_base
            rw_to_program(process_array, pos, values[2])
            # print("Adding {} and {} up. Writing {} to position {}".format(values[0], values[1], values[2], process_array[process_array[current_index + 3]]))
            increment = 4
        # Multiply
        elif opcode[-1] == '2':
            values[2] = values[0] * values[1]
            if params[2] == 0:
                pos = rw_to_program(process_array, current_index + 3)
            elif params[2] == 2:
                pos = rw_to_program(process_array, current_index + 3) + relative_base
            rw_to_program(process_array, pos, values[2])
            # print("Multiplying {} and {}. Writing {} to position {}".format(values[0], values[1], values[2], process_array[process_array[current_index + 3]]))
            increment = 4
        # Input
        elif opcode[-1] == '3':
            if params[0] == 0:
                pos = rw_to_program(process_array, current_index + 1)
            elif params[0] == 2:
                pos = rw_to_program(process_array, current_index + 1) + relative_base
            rw_to_program(process_array, pos, input_signal)
            # print("Received input {}. Writing it to position {}".format(user_input, process_array[current_index + 1]))
            increment = 2
        # Output
        elif opcode[-1] == '4':
            print("Output signal {}".format(values[0]))
            increment = 2
        elif opcode[-1] == '5':
            if values[0] != 0:
                if params[1] == 0:
                    pos = rw_to_program(process_array, current_index + 2)
                elif params[1] == 1:
                    pos = current_index + 2
                elif params[1] == 2:
                    pos = rw_to_program(process_array, current_index + 2) + relative_base
                increment = rw_to_program(process_array, pos)
                jump = True
            else:
                increment = 3
        elif opcode[-1] == '6':
            if values[0] == 0:
                if params[1] == 0:
                    pos = rw_to_program(process_array, current_index + 2)
                elif params[1] == 1:
                    pos = current_index + 2
                elif params[1] == 2:
                    pos = rw_to_program(process_array, current_index + 2) + relative_base
                increment = rw_to_program(process_array, pos)
                jump = True
            else:
                increment = 3
        elif opcode[-1] == '7':
            if params[2] == 0:
                pos = rw_to_program(process_array, current_index + 3)
            elif params[2] == 1:
                pos = current_index + 3
            elif params[2] == 2:
                pos = rw_to_program(process_array, current_index + 3) + relative_base
            if values[0] < values[1]:
                rw_to_program(process_array, pos, 1)
            else:
                rw_to_program(process_array, pos, 0)
            increment = 4
        elif opcode[-1] == '8':
            if params[2] == 0:
                pos = rw_to_program(process_array, current_index + 3)
            elif params[2] == 1:
                pos = current_index + 3
            elif params[2] == 2:
                pos = rw_to_program(process_array, current_index + 3) + relative_base
            if values[0] == values[1]:
                rw_to_program(process_array, pos, 1)
            else:
                rw_to_program(process_array, pos, 0)
            increment = 4
        elif opcode[-1:-3:-1] == '99':
            print("Halt initiated.")
            on_going = False
        elif opcode[-1] == '9':
            relative_base += values[0]
            increment = 2
        else:
            print("Unknown error, terminating")
            on_going = False
    return True


with open("09_input.txt", "r") as f:
    for line in f:
        string_array = line.split(",")

original_instructions = [int(i) for i in string_array]
run_program(original_instructions, 2)