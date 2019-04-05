from numpy import cos, sin, linspace,pi

import random

def style(size, colors, pixels):
    number_of_waves = random.randint(1,5)
    waves = []
    for i in range(number_of_waves):
        wave_properties = { 'a':random.uniform(.1,2),
                            'b':random.uniform(-2,2),
                            'c':random.uniform(-1,1),
                            'd': random.uniform(-4,4)
                             }# x coord, y coord, radius
        waves.append(wave_properties)

    x = linspace(-7,7,size[0])
    y = linspace(-4,4,size[1])

    values = []
    for wave in waves:
        for i in range(len(x)):
            for j in range(len(y)):
                theta = random.uniform(0, pi)
                if abs(wave['a']*sin(wave['b']*x[i]*cos(theta)-wave['c'])+wave['d']-y[j]*sin(theta))<0.05:
                    values.append([i,j])

    for i in range(len(values)):
        pixels[values[i][0], -values[i][1]]=colors[1]

    return pixels

