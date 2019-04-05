def set_palette():
    import palettes
    global colors
    colors = palettes.list[config['palette']]
    print(colors)

def set_style():
    global style
    if config['style'] == 'waves':
        from styles import waves
        style = waves.style
        print('waves')
    elif config['style'] == 'circles':
        from styles import circles
        style = circles.style
        print('cirlces')

def set_size():
    global size
    size = []
    size.append(config['size']['width'])
    size.append(config['size']['height'])
    size = tuple(size)
    print(size)

def draw_image():
    from PIL import Image
    from PIL import ImageFilter
    global img
    global pixels
    img = Image.new('RGB', size, colors[0])
    pixels = img.load()
    pixels = style(size, colors, pixels)
    img = img.filter(ImageFilter.SMOOTH_MORE)

def show_image():
    img.show()

def save_image():
    savename = config['palette'] + ' ' + config['style'] + ' ' + config['size'] + '.png'
    img.save(savename, 'PNG')

config = {'style': 'waves', 'palette': 'Red on white', 'size' : {'height' : 1080, 'width' : 1920}, 'lastmenu': 'palettes'}
set_palette()
set_style()
set_size()
draw_image()
show_image()
