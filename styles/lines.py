from numpy import linspace

import random

def style(size, colors, pixels):
    number_of_triangles = random.randint(1,5)
    triangles = []
    for i in range(number_of_triangles):
        triangle_properties = { 'a':{'x':random.uniform(-7,7),
                                    'y':random.uniform(-4,4)
                                    },
                                'b':{'x':random.uniform(-7,7),
                                    'y':random.uniform(-4,4)
                                    },
                                'c':{'x':random.uniform(-7,7),
                                    'y':random.uniform(-4,4)
                                    },
                             }# x coord, y coord, radius
        triangles.append(triangle_properties)

    x = linspace(-7,7,size[0])
    y = linspace(-4,4,size[1])
    values = []
    for triangle in triangles:
        for i in range(len(x)):
            for j in range(len(y)):
                if abs((triangle['b']['y']-triangle['c']['y'])/(triangle['b']['x']-triangle['c']['x'])*(x[i]-triangle['c']['x'])-(y[j]-triangle['c']['y']))<0.05:
                    values.append([i,j])

    for i in range(len(values)):
        pixels[values[i][0], -values[i][1]]=colors[1]

    return pixels

