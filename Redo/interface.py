#layout:
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

"""
Need to make sure defined variables are not stuck in local scopes
"""

#import os # for cls

pallettes = [
    {
    'name' : 'Red on white',
    'value' : ((255, 255, 255), (244, 66, 53))
    },
    {
    'name' : 'Blue on white',
    'value' : ((255, 255, 255), (66, 53, 244))
    },
    {
    'name' : 'Green on white',
    'value' : ((255, 255, 255), (53, 244, 66))
    }
    ]

class styles:
    list = [wave, cirlces]
    def wave():
        x = int(img.size[0]/2) # FIXME:
        y = int(img.size[1]/2) # FIXME:
        #drawing
        for i in range(img.size[0]):    # For every pixel:
            for j in range(img.size[1]):
                for p in range(num): #shadow business creates gradiant, very slow for some reason...
                    if j > (math.cos(i/200)*(y-400)) + y + p:
                        pixels[i,-j] = (pallette['value'][0][0] + p, pallette['value'][0][1] + p, pallette['value'][0][2] + p)
                if j < (math.cos(i/(y/2))*(y-y))+y: #cosine wave
                    pixels[i,-j-1] = pallette['value'][1]

    def circles():
        pass

def set_pallette():
    global pallette
    pallette = pallettes[a]
    print("Select a pallette:")
    options = []
    for i, v in enumerate(pallettes):
        print(str(i + 1) + '.\t' + v['name'])
        options.append(i)
    print("0.\tGo back")
    a = input("Selection: ")
    try:
        if int(a) - 1 in options:
            settings.set_pallette(int(a) - 1)
        elif a == '0':
            mainmenu()
        else:
            print("Selection not recognized")
            pallettepreview()
    except:
        print("Selection not recognized")
        pallettepreview()

def set_style():
    pass

def set_size():
    pass

def draw_image():
    pass

def save_image():
    print('Would you like to save the image? y/n')
    savedecision = input().upper()
    if savedecision == 'Y':
        savename = input('Please give a name for the save: ')
        img.save(savename + ".png", "PNG") #save image
        print('saved as', savename + '.png')
        mainmenu()
    elif savedecision == 'N':
        mainmenu()
    else:
        print("Selection not recognized")

def mainmenu():
    #os.system('cls' if os.name == 'nt' else 'clear') #taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python#2084628
    print("Make a selection:")
    print("1.\tpreview pallettes")
    print("2.\tgenereate image")
    print("0.\texit")
    testormake = input("Selection: ")
    if testormake == '1':   #preview pallettes
        pallettepreview()
    elif testormake == '2': #make image
        makeimage()
    elif testormake == '0': #exit
        print("exiting")
        exit()
    else:
        testormake = ''
        print("Selection not recognized")

def makeimage():
    print("Select a style:")
    for i, v in enumerate(styles.list):

    print("0.\tgo back")
    global imagestyle
    imagestyle = input("Selection: ")
    if int(imagestyle) in range(i+2):
        makeimage2() # FIXME: temp name
    elif imagestyle == '0':
        imagestyle = ''
        mainmenu()
    else:
        print("Selection not recognized")
        imagestyle = ''

def makeimage2(): # FIXME: temp name
    print("Select a pallette:") # FIXME: add pallette selection
    options = []
    for i, v in enumerate(pallettes):
        print(str(i + 1) + '.\t' + v['name'])
        options.append(i)
    print("0.\tGo back")
    global imagepallette
    imagepallette = input("Selection: ")
    if imagepallette - 1 in options
        makeimage3() # FIXME: temporary name
    elif imagepallette == '0':
        imagepallette = ''
        makeimage()
    else:
        print("Selection not recognized")
        imagepallette = ''

def makeimage3(): # FIXME: temp name
    print("Define horizontal image size")
    imagex = int(input("Width: ")) # FIXME: need to check if numbers
    imagey = int(input("Height: "))
    print("\"" + imagex + "x" + imagey + "\"")
    sizeyn = input("Is this correct? (y/n)").upper()
    if sizeyn == "Y":
        from PIL import Image
        from PIL import ImageFilter
        import math
        global size
        size = (imagex, imagey)
        pallette = pallettes.redwhite['values'] # FIXME: pallette selection
        img = Image.new( 'RGB', size, pallette)
        pixels = img.load()
        if imagestyle == '1': # FIXME: waves
            import waves
            print()
        elif imagestyle == '2': # FIXME: circles
            import circles
        img = img.filter(ImageFilter.SMOOTH_MORE)
        print("Loading preview")
        img.show()
        save_image()
    elif sizeyn == "N":
        sizeyn = ''
        makeimage3() # FIXME: temp name
    else:
        print("Selection not recognized")
        sizeyn = ''
        makeimage3() # FIXME: temp name

def pallettepreview():
    set_pallette()

mainmenu()
print(pallet)
exit()
