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
Need a better way to read the styles and pallettes,
generate selection lists, and interface with them.
"""

#import os #for cls
import pallettes

while True:
    #os.system('cls' if os.name == 'nt' else 'clear') #taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python#2084628
    print("Make a selection:")
    print("1.\tpreview pallettes")
    print("2.\tgenereate image")
    print("0.\texit")
    testormake = input("Selection: ")
    if testormake == '1':   #preview pallettes
        while True:
            print("Select a pallette:")
            print("1.\tRed on white")
            print("2.\tBlue on white")
            print("3.\tGreen on white")
            print("0.\tGo back")
            pallettepreview = input("Selection: ")
            if pallettepreview == '1': #red/white
                print()
                # FIXME:
            elif pallettepreview == '2': #blue/white
                print()
                # FIXME:
            elif pallettepreview == '3': #Green/white
                print()
                # FIXME:
            elif pallettepreview == '0':
                pallettepreview = ''
                break
            else:
                print("Selection not recognized")
    elif testormake == '2': #make image
        while True:
            print("Select a style:")
            print("1.\twaves")
            print("2.\tcircles")
            print("0.\tgo back")
            imagestyle = input("Selection: ")
            if imagestyle == '1' or imagestyle =='2': #continue
                while True:
                    print("Select a pallette:")
                    print("1.\tRed on white")
                    print("2.\tBlue on white")
                    print("3.\tGreen on white")
                    print("0.\tGo back")
                    imagepallette = input("Selection: ")
                    if imagepallette == '1' or imagepallette == '2' or imagepallette == '3':
                        while True: # FIXME: add pallette selection
                            print("Define horizontal image size")
                            imagex = int(input("Width: ")) # FIXME: need to check if numbers
                            imagey = int(input("Height: "))
                            print("\"" + imagex + "x" + imagey + "\"")
                            sizeyn = input("Is this correct? (y/n)").upper()
                            if sizeyn == "Y":
                                from PIL import Image
                                from PIL import ImageFilter
                                import math
                                size = (imagex, imagey)
                                pallette = # FIXME: pallette selection
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
                                        print("Selection not recognized")
                            elif sizeyn == "N"
                                sizeyn = ''
                            else:
                                print("Selection not recognized")
                                sizeyn = ''
                    elif imagepallette == '0':
                        imagepallette = ''
                        break
                    else:
                        print("Selection not recognized")
                        imagepallette = ''
            elif imagestyle == '0':
                imagestyle = ''
                break
            else:
                print("Selection not recognized")
                imagestyle = ''
    elif testormake == '0': #exit
        Print("exiting")
        exit()
    else:
        testormake = ''
        print("Selection not recognized")
exit()
