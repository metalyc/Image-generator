def set_palette(x):
    import palettes
    global colors
    colors = palettes.list[x]
    print(colors)

def set_style(x):
    global style
    if x == 'waves':
        from styles import waves
        style = waves.style
        print('waves')
    elif x == 'circles':
        from styles import circles
        style = circles.style
        print('cirlces')

def set_size(x):
    global size
    size = []
    size.append(x['width'])
    size.append(x['height'])
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

def generate(config):
    set_palette(config['palette'])
    set_style(config['style'])
    set_size(config['size'])
    draw_image()
    show_image()
