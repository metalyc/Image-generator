from PIL import Image
from PIL import ImageFilter
import math
import random

pallet = ((0, 0, 0), (120, 220, 65), (255, 0, 0))
size = (1920, 1080)
num_circles = random.randint(1, 10)
circles = {}

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

for i in range(img.size[0]):
    for j in range(img.size[1]):
    	c_key = ' '.join(str(e) for e in [i, j])
    	if c_key in circles:
    		r = circles[c_key]
    		for looper in range(r*2):
    			y_c = looper + (j - r)
    			x_c = math.floor(math.sqrt(r**2 - (y_c - j)**2) + i)
    			print_pixel(x_c, y_c)
    			x_c = math.floor(math.sqrt(r**2 - (y_c - j)**2) * -1 + i)
    			print_pixel(x_c, y_c)

    		for looper in range(r*2):
    			x_c = looper + (i - r)
    			y_c = math.floor(math.sqrt(r**2 - (x_c - i)**2) + j)
    			print_pixel(x_c, y_c)
    			y_c = math.floor(math.sqrt(r**2 - (x_c - i)**2) * -1 + j)
    			print_pixel(x_c, y_c)

img = img.filter(ImageFilter.SMOOTH_MORE)

img.show()