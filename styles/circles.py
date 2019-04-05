from numpy import linspace
import random

def style(size, colors, pixels):
    number_of_circles = random.randint(1,5)
    circles = []
    for i in range(number_of_circles):
        circle_properties = {'x':random.uniform(-7,7),
                             'y':random.uniform(-4,4),
                             'r':random.uniform(.5,2)
                             }# x coord, y coord, radius
        circles.append(circle_properties)
    print(circles[0]['x'])
    x = linspace(-7,7,size[0])
    y = linspace(-4,4,size[1])
    values = []
    for circle in circles:
        for i in range(len(x)):
            for j in range(len(y)):
                if (x[i]-circle['x'])**2+(y[j]-circle['y'])**2-circle['r']**2<0.00000001:
                    values.append([i,j])

    for i in range(len(values)):
        pixels[values[i][0], -values[i][1]]=colors[1]

    return pixels

