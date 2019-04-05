def set_palette(x):
    import palettes
    global colors
    colors = palettes.p_list[x]
    print('palette:', x, colors)

def set_style(x):
    global style
    if x == 'waves':
        from styles import waves
        style = waves.style
    elif x == 'circles':
        from styles import circles
        style = circles.style
    elif x == 'heart':
        from styles import heart
        style = heart.style
    elif x == 'wonkylines':
        from styles import wonkylines
        style = wonkylines.style
    elif x == 'lines':
        from styles import lines
        style = lines.style
    elif x == 'wavesRandom':
        from styles import wavesRandom
        style = wavesRandom.style
    elif x == 'puddle':
        from styles import puddle
        style = puddle.style
    elif x == 'randomParticle':
        from styles import randomParticle
        style = randomParticle.style
    print('style:', x)

def set_size(x):
    global size
    size = []
    size.append(x['width'])
    size.append(x['height'])
    size = tuple(size)
    print('resolution:', size)

def draw_image():
    print('Drawing image...')
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
    print('Image saved in \"images\" folder, as \"' + savename + '\"')

def generate(config):
    set_palette(config['palette'])
    set_style(config['style'])
    set_size(config['size'])
    draw_image()
    show_image()
    save_image(config)
