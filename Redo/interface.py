#interface
    #test pallets
        #list pallettes
    #make image
        #select style
            #list styles
        #select pallette
            #list pallettes
        #set image size
        #confirm settings
            #demo
        #draw image
        #show image
        #options for saving and name
import os
import pallettes

while True:
    #os.system('cls' if os.name == 'nt' else 'clear') #taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python#2084628
    print("Make a selection:")
    print("1.\tpreview pallettes")
    print("2.\tgenereate image")
    print("0.\texit")
    testormake = input("Selection: ")
    if testormake == '1':
        print("Select a pallette:")
        print("1.\tRed on white")
        print("2.\tBlue on white")
        print("3.\tGreen on white")
        print("0.\tGo back")
        pallettepreview = input("Selection: ")
        if pellettepreview == '1':
            print()
            # FIXME: finish this shit
        else:
            pass
    elif testormake == '2':
        print()
        # FIXME: shit
    elif testermake == '0':
        exit()
    else:
        print("not recognized.")
        pass

#setup
from PIL import Image
from PIL import ImageFilter
import math
img = Image.new( 'RGB', set.size, set.pallet[0]) # FIXME:
pixels = img.load()
x = int(img.size[0]/2) # FIXME:
y = int(img.size[1]/2) # FIXME:

#drawing
for i in range(img.size[0]):    # For every pixel:
    for j in range(img.size[1]):
        for p in range(num): #shadow business creates gradiant, very slow for some reason...
            if j > (math.cos(i/200)*(y-400)) + y + p:
                pixels[i,-j] = (set.pallet[0][0] + p, set.pallet[0][1] + p, set.pallet[0][2] + p)
        if j < (math.cos(i/(y/2))*(y-y))+y: #cosine wave
            pixels[i,-j-1] = set.pallet[1]

#finishing
img = img.filter(ImageFilter.SMOOTH_MORE) #filter

print('Image finished!')
img.show() #show image
while True:
    print('Would you like to save the image? y/n')
    savedecision = input().upper()
    if savedecision == 'Y':
        savename = input('Please give a name for the save: ')
        img.save(savename + ".png", "PNG") #save image
        print('saved as', savename + '.png')
        break
    elif savedecision == 'N':
        break
    else:
        print("input not recognized")

print('exiting')
