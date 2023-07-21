from PIL import Image
import sys

if len(sys.argv) < 3:
    exit()

input_image = Image.open(sys.argv[1])

input_pixel_map = input_image.load()

src_width, src_height = input_image.size

width = src_width * 3
height = src_height * 3

output_image = Image.new(mode="RGBA", size=(width, height), color=(0,0,0,0))

output_pixel_map = output_image.load()

for y in range(src_height):
    for x in range(src_width):
        output_pixel_map[x*3 + 1, y*3 + 1] = input_pixel_map[x,y]

output_image.save(sys.argv[2])