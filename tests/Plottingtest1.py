from PIL import Image
from PIL import ImageFilter
import math

class set:
    pallet = ((0, 0, 0), (255,255,255), (255, 0, 0)) #((255, 255, 255), (244, 67, 54))
    size = (800, 800)

print("Creating image...")
img = Image.new( 'RGB', set.size, set.pallet[1]) # Create a new image (in this case 1920x1080, off-white)
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
        if j == y:
            pixels[i,-j-1] = set.pallet[0]
        if i == x:
            pixels[i,-j-1] = set.pallet[0]
        if j == i:
            pixels[i,-j-1] = set.pallet[2]
print("done.")

print("Starting filters...")
img = img.filter(ImageFilter.SMOOTH_MORE) #filter
print("done.")

print("Creating file...")
img.show() #show image
#img.save("test.png", "PNG") #save image
print("done.")
