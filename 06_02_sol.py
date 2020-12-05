space_objects = {}
total_orbiters = 0
paths = []
you_orbit = ""
san_orbit = ""

# def count_orbiters(so):
#     current_orbiters = len(space_objects[so])
#     for x in space_objects[so]:
#         if x in space_objects:
#             current_orbiters += count_orbiters(x)
#     return current_orbiters


def find_paths(starting_name, current_path, end_target):
    starting_path = current_path
    for orbiter in space_objects[starting_name][0]:
        if orbiter in current_path:
            paths.append(current_path)
        else:
            current_path = starting_path + "-" + orbiter
            find_paths(orbiter, current_path, end_target)
    for orbiting in space_objects[starting_name][1]:
        if orbiting in current_path:
            if current_path not in paths:
                paths.append(current_path)
        else:
            current_path = starting_path + "-" + orbiting
            find_paths(orbiting, current_path, end_target)


with open("06_input.txt", "r") as f:
    for line in f:
        object_name, orbiter_name = line.rstrip().split(")")
        if orbiter_name == "YOU":
            you_orbit = object_name
        if orbiter_name == "SAN":
            san_orbit = object_name
        if object_name in space_objects:
            space_objects[object_name][0].append(orbiter_name)
        else:
            space_objects[object_name] = [[orbiter_name], []]
        if orbiter_name in space_objects:
            space_objects[orbiter_name][1].append(object_name)
        else:
            space_objects[orbiter_name] = [[], [object_name]]

# for so in list(space_objects):
#     current_orbiters = count_orbiters(so)
#     total_orbiters += current_orbiters

# print(total_orbiters)

find_paths("YOU", "YOU", "SAN")

for path in paths:
    x = path.split("-")
    if x[-1] == "SAN":
        print(len(x)-3)
# for path in paths:
#     x = path.split('-')
#     if x[0] == you_orbit and x[-1] == san_orbit:
#         print(path)