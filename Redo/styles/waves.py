#waves plotting here
#should only plot the wave and shadow, not the background
#options:
    #height (from valley to peak)
    #bite (space between peaks)
    #padding from top and bottom
    #shadow intensity

#below is an old version
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
