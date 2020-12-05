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

def decode_layers(image):
    height = len(image[0])
    width = len(image[0][0])
    current_image = image[0].copy()

    for i in range(height):
        for j in range(width):
            if current_image[i][j] == 2:
                for layer in image:
                    if layer[i][j] != 2:
                        current_image[i][j] = layer[i][j]
                        break
    return current_image


with open("08_input.txt", "r") as f:
    for line in f:
        string_array = line
    for char in string_array:
        pixels.append(int(char))

image = get_image(25, 6, pixels)

result = decode_layers(image)
for row in result:
    image_row = ""
    for char in row:
        if char == 0:
            image_row += ' '
        else:
            image_row += '1'
    print(image_row)
