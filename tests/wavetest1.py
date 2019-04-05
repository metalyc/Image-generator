print("Setting up parameters...")
from PIL import Image
from PIL import ImageFilter
import math

class set:
    pallet = ((255, 255, 255), (244, 67, 54))
    size = (1920, 1080)

img = Image.new( 'RGB', set.size, set.pallet[0]) # Create a new image (in this case 1920x1080, off-white)
pixels = img.load() # Create the pixel map
x = int(img.size[0]/2) #parameters for the center of the image
y = int(img.size[1]/2)
print("done.")

print("Drawing image...")
for i in range(img.size[0]):    # For every pixel:
    for j in range(img.size[1]):
        for p in range(50): #shadow business creates gradiant, very slow for some reason...
            if j > (math.cos(i/200)*(y-400)) + y + p:
                pixels[i,-j] = (set.pallet[0][0] + p, set.pallet[0][1] + p, set.pallet[0][2] + p)
        if j < (math.cos(i/200)*(y-400))+y: #cosine wave
            pixels[i,-j-1] = set.pallet[1]
print("done.")

print("Starting filters...")
img = img.filter(ImageFilter.SMOOTH_MORE) #filter
print("done.")

print("Creating file...")
#img.show() #show image
img.save("test.png", "PNG") #save image
print("done.")
