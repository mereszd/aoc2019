space_objects = {}
total_orbiters = 0

def count_orbiters(so):
    current_orbiters = len(space_objects[so])
    for x in space_objects[so]:
        if x in space_objects:
            current_orbiters += count_orbiters(x)
    return current_orbiters


with open("06_input.txt", "r") as f:
    for line in f:
        object_name, orbiter_name = line.rstrip().split(")")
        if object_name in space_objects:
            space_objects[object_name].append(orbiter_name)
        else:
            space_objects[object_name] = [orbiter_name]

for so in list(space_objects):
    current_orbiters = count_orbiters(so)
    total_orbiters += current_orbiters

print(total_orbiters)