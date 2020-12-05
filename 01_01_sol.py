input_array = []
sum = 0

with open("01_01_input.txt", "r") as f:
    for x in f:
        input_array.append(int(x.strip()))

for x in input_array:
    sum = sum + (x//3 - 2)
print(sum)