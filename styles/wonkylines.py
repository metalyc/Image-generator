from numpy import linspace, sin

def style(size, colors, pixels):
    x = linspace(-7,7,size[0])
    y = linspace(-4,4,size[1])
    values = []
    for i in range(len(x)):
        for j in range(len(y)):
            if abs(sin(x[i]**2+2*x[i]*y[j]))-sin(x[i]-2*y[j])< 0.00001:
                values.append([i,j])

    for i in range(len(values)):
        pixels[values[i][0], -values[i][1]]=colors[1]

    return pixels