import itertools
import threading
import time


def get_input(name):
    item_found = False
    sleep_amount = 0.1
    times_sleeped = 0
    while item_found is False:
        for item in queue:
            if item[0] == name:
                input_signal = item[1]
                queue.remove(item)
                item_found = True
                # print(
                #     "{} retrieved {} from the queue. State of the queue is {} "
                #     .format(name, item, queue))
                break
    if times_sleeped == 9:
        print("{} tried to retrieve an input_signal, but couldn't find in queue after 10 tries. Current state of "
              "queue is {} "
              .format(name, queue))
    if item_found is False:
        print("{} tried to retrieve an input_signal, but couldn't find in queue. Sleeping for {}"
              .format(name, sleep_amount))
        time.sleep(sleep_amount)
        times_sleeped += 1
        sleep_amount *= 2
    return input_signal


def post_input(name, input_signal):
    queue.append([Amp_Dict[name], input_signal])
    # print("{} added {} to the queue. Current state of queue is {}".format(name, [Amp_Dict[name], input_signal], queue))
    return True


def run_program(name, process_array, phase_setting):
    # print("{} starting.".format(name))
    current_index = 0
    on_going = True
    jump = False
    increment = 0
    skip_ps = False
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
            if skip_ps:
                user_input = get_input(name)
                # print("{} received Input signal {}".format(name, user_input))
            else:
                user_input = phase_setting
                skip_ps = True
                # print("{} received Phase setting {}".format(name, user_input))
            process_array[process_array[current_index + 1]] = user_input
            # print("Received input {}. Writing it to position {}".format(user_input, process_array[current_index + 1]))
            increment = 2
        elif opcode[-1] == '4':
            if params[0] == 0:
                values[0] = process_array[process_array[current_index + 1]]
            else:
                values[0] = process_array[current_index + 1]
            # print("{} submitting output signal {}".format(name, values[0]))
            post_input(name, values[0])
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
            # print("Halt initiated.")
            on_going = False
        else:
            print("Unknown error, terminating")
            on_going = False
    return output_signal


string_array = []
Amp_Dict = {
    "AmpA": "AmpB",
    "AmpB": "AmpC",
    "AmpC": "AmpD",
    "AmpD": "AmpE",
    "AmpE": "AmpA"
}

with open("07_input.txt", "r") as f:
    for line in f:
        string_array = line.split(",")

original_instructions = [int(i) for i in string_array]

available_phase_settings = set(itertools.permutations([5, 6, 7, 8, 9]))

max_output_signal = 0
for aps in available_phase_settings:
    queue = [["AmpA", 0]]
    threads = []
    AmpA = threading.Thread(target=run_program, args=("AmpA", original_instructions.copy(), aps[0]))
    AmpB = threading.Thread(target=run_program, args=("AmpB", original_instructions.copy(), aps[1]))
    AmpC = threading.Thread(target=run_program, args=("AmpC", original_instructions.copy(), aps[2]))
    AmpD = threading.Thread(target=run_program, args=("AmpD", original_instructions.copy(), aps[3]))
    AmpE = threading.Thread(target=run_program, args=("AmpE", original_instructions.copy(), aps[4]))
    threads.append(AmpA)
    threads.append(AmpB)
    threads.append(AmpC)
    threads.append(AmpD)
    threads.append(AmpE)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # print("Threads finished for phase settings {}. Output voltage is {}".format(aps, queue[0][1]))
    if queue[0][0] == "AmpA":
        current_output_signal = queue[0][1]
        if current_output_signal > max_output_signal:
            max_output_signal = current_output_signal
            best_aps = aps

print("Highest output signal found is {} for config {}".format(max_output_signal, best_aps))