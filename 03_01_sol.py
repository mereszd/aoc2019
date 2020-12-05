dir_wire_1 = []
dir_wire_2 = []
points_wire_1 = []
points_wire_2 = []
just_points_1 = []
just_points_2 = []
points_distance = []
steps_distance = []
on_going = True


def add_point (points_wire, current_point, step):
    to_add = "X" + str(current_point[0]) + "Y" + str(current_point[1]) + "S" + str(step)
    points_wire.append(to_add)
    return points_wire


def calc_points(dir_wire, points_wire):
    current_point = [0, 0]
    step = 0
    points_wire = add_point(points_wire, current_point, step)
    for dir in dir_wire:
        if dir[0] == 'U':
            mov = int(dir[1:])
            for i in range(mov):
                current_point[1] = current_point[1] + 1
                step += 1
                points_wire = add_point(points_wire, current_point, step)
        elif dir[0] == 'D':
            mov = int(dir[1:])
            for i in range(mov):
                current_point[1] = current_point[1] - 1
                step += 1
                points_wire = add_point(points_wire, current_point, step)
        elif dir[0] == 'L':
            mov = int(dir[1:])
            for i in range(mov):
                current_point[0] = current_point[0] - 1
                step += 1
                points_wire = add_point(points_wire, current_point, step)
        elif dir[0] == 'R':
            mov = int(dir[1:])
            for i in range(mov):
                current_point[0] = current_point[0] + 1
                step += 1
                points_wire = add_point(points_wire, current_point, step)
    return points_wire

with open("03_input.txt", "r") as f:
    line = f.readline()
    dir_wire_1 = line.split(",")
    dir_wire_1[len(dir_wire_1)-1] = dir_wire_1[len(dir_wire_1)-1].replace('\n', '')
    line = f.readline()
    dir_wire_2 = line.split(",")

calc_points(dir_wire_1, points_wire_1)
calc_points(dir_wire_2, points_wire_2)

for point in points_wire_1:
    just_point, step = point.split('S')
    just_points_1.append(just_point)

for point in points_wire_2:
    just_point, step = point.split('S')
    just_points_2.append(just_point)

print("finished calc")
common_points = list(set(just_points_1) & set(just_points_2))

for p in range(len(common_points)):
    for i in points_wire_1:
        if common_points[p] + "S" in i:
            _temp, step = i.split('S')
            steps_distance.append(int(step))
            print("Found {} in {}, step is {}, step distance is {}".format(common_points[p], i, step, steps_distance[p]))
            break
    for j in points_wire_2:
        if common_points[p] + "S" in j:
            _temp, step = j.split('S')
            steps_distance[p] = steps_distance[p] + int(step)
            print("Found {} in {}, step is {}, step distance is {}".format(common_points[p], i, step, steps_distance[p]))
            break

steps_distance.remove(0)
print(min(steps_distance))