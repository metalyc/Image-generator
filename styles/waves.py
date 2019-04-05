def style(size, colors, pixels):
    import math
    x = math.floor(size[0]/2)
    y = math.floor(size[1]/2)
    shadowlen = 25
    y_tl = y*0.75
    y_tm = y*0.375
    for i in range(size[0]):
        wave_algo = (math.cos(i/(y_tm))*(y-y_tl)) + y
        for j in range(size[1]):
            for s in range(shadowlen):
                if wave_algo + s + 1 > j > wave_algo + s:
                    q = math.floor(s*(shadowlen/10) + y_tm)
                    pixels[i,-j-1] = (abs(pixels[i,-j-1][0] - 255 + q), abs(pixels[i,-j-1][1] - 255 + q), abs(pixels[i,-j-1][2] - 255 + q))
            if j < wave_algo:
                pixels[i,-j-1] = colors[1]
    return pixels
