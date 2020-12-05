input = "206938-679128"
min_value, max_value = input.split('-')
min_value = int(min_value)
max_value = int(max_value)
count = 0

def check_consecutive(value):
    consec = False
    str_value = str(value)
    for i in range(len(str_value)-1):
        if str_value[i] == str_value[i+1]:
            consec = True
            break
    return consec

def check_increase(value):
    inc = True
    str_value = str(value)
    for i in range(len(str_value)-1):
        if int(str_value[i]) > int(str_value[i+1]):
            inc = False
            break
    return inc

for i in range(min_value, max_value+1):
    if check_consecutive(i) and check_increase(i):
        count += 1

print(count)