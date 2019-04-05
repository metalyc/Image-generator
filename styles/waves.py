#waves plotting here
#should only plot the wave and shadow, not the background
#options:
    #height (from valley to peak)
    #bite (space between peaks)
    #padding from top and bottom
    #shadow intensity
def style(size, colors, pixels):
    import math
    x = math.floor(size[0]/2)
    y = math.floor(size[1]/2)
    shadowlen = 25 # FIXME: might need to scale
    for i in range(size[0]):
        for j in range(size[1]):
            for s in range(shadowlen):
                if (math.cos(i/(y*0.375))*(y-y*0.75)) + y + s + 1 > j > (math.cos(i/(y*0.375))*(y-y*0.75)) + y + s:
                    q = s*2 + math.floor(y*0.375)
                    pixels[i,-j-1] = (abs(colors[0][0] - 255) + q, abs(colors[0][1] - 255) + q, abs(colors[0][2] - 255) + q)
            if j < (math.cos(i/(y*0.375))*(y-y*0.75))+y:
                pixels[i,-j-1] = colors[1]
    return pixels
