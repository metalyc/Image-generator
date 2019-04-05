from numpy import linspace
import random

def style(size, colors, pixels):
    x = linspace(-7,7,size[0])
    y = linspace(-4,4,size[1])
    x0= random.randint(size[0]/5,size[0]*4/5)
    y0= random.randint(size[1]/5,size[1]*4/5)
    values = []
    for i in range(len(x)):
        for j in range(len(y)):
            if ((x[i]**2) + (y[j])**2 -1)**3 -(x[i])**2 * (y[j]) **3 < 0.00000001:
                values.append([i-x0,j-y0])

    for i in range(len(values)):
        pixels[values[i][0], -values[i][1]]=colors[1]

    return pixels