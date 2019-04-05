from numpy import linspace

def style(size, colors, pixels):
    x = linspace(-7,7,size[0])
    y = linspace(-4,4,size[1])
    values = []
    for i in range(len(x)):
        for j in range(len(y)):
            if (x[i]**2 + y[j]**2 -1)**3 -x[i]**2 * y[j] **3 < 0.00000001:
                values.append([i,j])

    for i in range(len(values)):
        pixels[values[i][0], -values[i][1]]=colors[1]

    return pixels