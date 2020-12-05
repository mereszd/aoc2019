input_array = []
sum = 0


def calc_fuel(x):
    fuel = x//3-2
    if fuel > 0:
        fuel = fuel + calc_fuel(fuel)
    else:
        return 0
    return fuel


with open("01_01_input.txt", "r") as f:
    for x in f:
        input_array.append(int(x.strip()))

for x in input_array:
    sum = sum + calc_fuel(x)

print(sum)