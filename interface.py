def set_palette(x):
    import palettes
    global colors
    colors = palettes.p_list[x]
    print(x, colors)

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
    elif x == 'heart':
        from styles import heart
        style = heart.style
        print('heart')
    elif x == 'wonkylines':
        from styles import wonkylines
        style = wonkylines.style
        print('wonkylines')

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

def save_image(config):
    savename = config['palette'] + ' ' + config['style'] + ' ' + str(config['size']['width']) + 'x' + str(config['size']['height']) + '.png'
    img.save('generated images/' + savename, 'PNG')

def generate(config):
    print(config['palette'])
    set_palette(config['palette'])
    set_style(config['style'])
    set_size(config['size'])
    draw_image()
    show_image()
    save_image(config)
