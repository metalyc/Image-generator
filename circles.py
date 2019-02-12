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

print(circles)

for i in range(img.size[0]):
    for j in range(img.size[1]):
    	c_key = ' '.join(str(e) for e in [i, j])
    	if c_key in circles:
    		#print(' '.join(str(e) for e in [i, j]))
    		#print(i,j)
    		r = circles[c_key]
    		'''
    		for q in range(6):
    			for f in range(6):
    				pixels[i-3+q, j-3+f] = pallet[0]
    		'''
    		for looper in range(r*2):
    			y_c = looper + (j - r)
    			x_c = math.floor(math.sqrt(r**2 - (y_c - j)**2) + i)
    			
    			if x_c >= size[0] or y_c >= size[1] or x_c < 0 or y_c < 0:
    				pass
    			else:
    				pixels[x_c, y_c] = pallet[0]

    			x_c = math.floor(math.sqrt(r**2 - (y_c - j)**2) * -1 + i)

    			if x_c >= size[0] or y_c >= size[1] or x_c < 0 or y_c < 0:
    				pass
    			else:
    				pixels[x_c, y_c] = pallet[0]

    		for looper in range(r*2):
    			x_c = looper + (i - r)
    			y_c = math.floor(math.sqrt(r**2 - (x_c - i)**2) + j)
    			
    			if x_c >= size[0] or y_c >= size[1] or x_c < 0 or y_c < 0:
    				pass
    			else:
    				pixels[x_c, y_c] = pallet[0]

    			y_c = math.floor(math.sqrt(r**2 - (x_c - i)**2) * -1 + j)

    			if x_c >= size[0] or y_c >= size[1] or x_c < 0 or y_c < 0:
    				pass
    			else:
    				pixels[x_c, y_c] = pallet[0]

img = img.filter(ImageFilter.SMOOTH_MORE)

img.show()