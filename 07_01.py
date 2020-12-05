import itertools


def run_program(process_array, phase_setting, input_signal):
    current_index = 0
    on_going = True
    jump = False
    increment = 0
    second_input = False
    output_signal = 0
    while on_going:
        if jump:
            current_index = increment
            jump = False
        else:
            current_index += increment
        opcode = str(process_array[current_index])
        params = [0, 0, 0]
        values = [0, 0, 0]
        for i in range(3, len(opcode) + 1):
            params[i - 3] = int(opcode[-i])
        if opcode[-1] == '1':
            if params[0] == 0:
                values[0] = process_array[process_array[current_index+1]]
            else:
                values[0] = process_array[current_index + 1]
            if params[1] == 0:
                values[1] = process_array[process_array[current_index+2]]
            else:
                values[1] = process_array[current_index + 2]
            values[2] = values[0] + values[1]
            process_array[process_array[current_index + 3]] = values[2]
            # print("Adding {} and {} up. Writing {} to position {}".format(values[0], values[1], values[2], process_array[process_array[current_index + 3]]))
            increment = 4
        elif opcode[-1] == '2':
            if params[0] == 0:
                values[0] = process_array[process_array[current_index + 1]]
            else:
                values[0] = process_array[current_index + 1]
            if params[1] == 0:
                values[1] = process_array[process_array[current_index + 2]]
            else:
                values[1] = process_array[current_index + 2]
            values[2] = values[0] * values[1]
            process_array[process_array[current_index + 3]] = values[2]
            # print("Multiplying {} and {}. Writing {} to position {}".format(values[0], values[1], values[2], process_array[process_array[current_index + 3]]))
            increment = 4
        elif opcode[-1] == '3':
            if second_input:
                user_input = input_signal
                print("Received Input signal {}".format(user_input))
            else:
                user_input = phase_setting
                second_input = True
                print("Received Phase setting {}".format(user_input))
            process_array[process_array[current_index + 1]] = user_input
            # print("Received input {}. Writing it to position {}".format(user_input, process_array[current_index + 1]))
            increment = 2
        elif opcode[-1] == '4':
            if params[0] == 0:
                values[0] = process_array[process_array[current_index + 1]]
            else:
                values[0] = process_array[current_index + 1]
            print("Value: {}".format(values[0]))
            output_signal = values[0]
            increment = 2
        elif opcode[-1] == '5':
            if params[0] == 0:
                values[0] = process_array[process_array[current_index + 1]]
            else:
                values[0] = process_array[current_index + 1]
            if values[0] != 0:
                if params[1] == 0:
                    increment = process_array[process_array[current_index + 2]]
                else:
                    increment = process_array[current_index + 2]
                jump = True
            else:
                increment = 3
        elif opcode[-1] == '6':
            if params[0] == 0:
                values[0] = process_array[process_array[current_index + 1]]
            else:
                values[0] = process_array[current_index + 1]
            if values[0] == 0:
                if params[1] == 0:
                    increment = process_array[process_array[current_index + 2]]
                else:
                    increment = process_array[current_index + 2]
                jump = True
            else:
                increment = 3
        elif opcode[-1] == '7':
            if params[0] == 0:
                values[0] = process_array[process_array[current_index + 1]]
            else:
                values[0] = process_array[current_index + 1]
            if params[1] == 0:
                values[1] = process_array[process_array[current_index + 2]]
            else:
                values[1] = process_array[current_index + 2]
            if values[0] < values[1]:
                if params[2] == 0:
                    process_array[process_array[current_index + 3]] = 1
                else:
                    process_array[current_index + 3] = 1
            else:
                if params[2] == 0:
                    process_array[process_array[current_index + 3]] = 0
                else:
                    process_array[current_index + 3] = 0
            increment = 4
        elif opcode[-1] == '8':
            if params[0] == 0:
                values[0] = process_array[process_array[current_index + 1]]
            else:
                values[0] = process_array[current_index + 1]
            if params[1] == 0:
                values[1] = process_array[process_array[current_index + 2]]
            else:
                values[1] = process_array[current_index + 2]
            if values[0] == values[1]:
                if params[2] == 0:
                    process_array[process_array[current_index + 3]] = 1
                else:
                    process_array[current_index + 3] = 1
            else:
                if params[2] == 0:
                    process_array[process_array[current_index + 3]] = 0
                else:
                    process_array[current_index + 3] = 0
            increment = 4
        elif opcode[-1:-3:-1] == '99':
            print("Halt initiated.")
            on_going = False
            second_input = False
        else:
            print("Unknown error, terminating")
            on_going = False
            second_input = False
    return output_signal


string_array = []
with open("07_input.txt", "r") as f:
    for line in f:
        string_array = line.split(",")

original_instructions = [int(i) for i in string_array]

available_phase_settings = set(itertools.permutations([0, 1, 2, 3, 4]))

max_output_signal = 0
for aps in available_phase_settings:
    input_signal = 0
    for i in range(len(aps)):
        process_array = original_instructions.copy()
        output_signal = run_program(process_array, aps[i], input_signal)
        input_signal = output_signal
    if output_signal > max_output_signal:
        max_output_signal = output_signal

print(max_output_signal)