from PIL import Image
from PIL import ImageFilter
import math
import random

pallet = ((0, 0, 0), (120, 220, 65), (255, 0, 0))
size = (1920, 1080)
num_circles = random.randint(1, 10)
circles = {}
circle_thickness = 5

for x in range(num_circles):
	radius = random.randint(0, (size[0] // 4) )
	center = [random.randint(0, size[0]), random.randint(0, size[1])]
	circles[' '.join(str(e) for e in center)] = radius

img = Image.new('RGB', size, pallet[1])
pixels = img.load()

x = int(img.size[0]/2)
y = int(img.size[1]/2)

def print_pixel(x_c, y_c):
	if x_c >= size[0] or y_c >= size[1] or x_c < 0 or y_c < 0:
		pass
	else:
		pixels[x_c, y_c] = pallet[0]

def print_block(x_c, y_c, t_t):
	for x in range(t_t):
		for y in range(t_t):
			print_pixel(x_c-1+x, y_c-1+y)

for i in range(img.size[0]):
    for j in range(img.size[1]):
    	c_key = ' '.join(str(e) for e in [i, j])
    	if c_key in circles:
    		r = circles[c_key]
    		for looper in range(r*2):
    			y_c = looper + (j - r)
    			x_c = math.floor(math.sqrt(r**2 - (y_c - j)**2) + i)
    			print_block(x_c, y_c, circle_thickness)
    			x_c = math.floor(math.sqrt(r**2 - (y_c - j)**2) * -1 + i)
    			print_block(x_c, y_c, circle_thickness)

    		for looper in range(r*2):
    			x_c = looper + (i - r)
    			y_c = math.floor(math.sqrt(r**2 - (x_c - i)**2) + j)
    			print_block(x_c, y_c, circle_thickness)
    			y_c = math.floor(math.sqrt(r**2 - (x_c - i)**2) * -1 + j)
    			print_block(x_c, y_c, circle_thickness)

img = img.filter(ImageFilter.SMOOTH_MORE)

img.show()