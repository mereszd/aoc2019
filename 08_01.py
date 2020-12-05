pixels = []


def get_image(width, height, pixels):
    image = []
    pixel_pointer = 0
    while pixel_pointer < len(pixels)-1:
        layer = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(pixels[pixel_pointer])
                pixel_pointer += 1
            layer.append(row)
        image.append(layer)

    return image



with open("08_input.txt", "r") as f:
    for line in f:
        string_array = line
    for char in string_array:
        pixels.append(int(char))

image = get_image(25, 6, pixels)

least_0 = [999, 999]

for i in range(len(image)):
    zeros = 0
    ones = 0
    twos = 0
    for j in range(len(image[i])):
        zeros += image[i][j].count(0)
        ones += image[i][j].count(1)
        twos += image[i][j].count(2)
    if zeros < least_0[1]:
        least_0 = [i, zeros, ones, twos]

print(least_0[2] * least_0[3])