from PIL import Image
from PIL import ImageFilter
import math

print("Creating image...")
img = Image.new( 'RGB', (1920, 1080), (250, 250, 250)) # Create a new image (in this case 1920x1080, off-white)
print("done.")
print("Creating pixel map...")
pixels = img.load() # Create the pixel map
print("done.")
print("Setting parameters...")
x = int(img.size[0]/2) #parameters for the center of the image
y = int(img.size[1]/2)
print("done.")

print("Drawing image...")
for i in range(img.size[0]):    # For every pixel:
    for j in range(img.size[1]):
        p = 0
        for p in range(50): #shadow business, creates gradiant, very slow for some reason...
            if j > y + p:
                q = p + 200
                pixels[i,-j] = (q, q, q)
        if j < y: #half red
            pixels[i,-j-1] = (255, 0, 0)
print("done.")

print("Starting filters...")
img = img.filter(ImageFilter.SMOOTH_MORE) #filter
print("done.")

print("Creating file...")
img.show() #show image
#img.save("test.png", "PNG") #save image
print("done.")
