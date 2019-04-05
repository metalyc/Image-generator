from numpy import linspace, sin, cos,pi
import random

def style(size, colors, pixels):
    x = linspace(-7,7,size[0])
    y = linspace(-4,4,size[1])
    theta = random.uniform(0,pi)
    values = []
    for i in range(len(x)):
        for j in range(len(y)):
            if abs(sin((x[i]*cos(theta))**2+2*(x[i]*cos(theta))*(y[j]*sin(theta))))-sin((x[i]*cos(theta))-2*(y[j]*sin(theta)))< 0.00001:
                values.append([i,j])

    for i in range(len(values)):
        pixels[values[i][0], -values[i][1]]=colors[1]

    return pixels