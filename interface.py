#layout:
    #test pallets
        #list pallettes
    #make image
        #select style
            #list styles
        #select pallette
            #list pallettes
        #set image size
        #confirm settings
            #demo
        #draw image
        #show image
        #options for saving and name

"""
Need a better way to read the styles and pallettes,
generate selection lists, and interface with them.
"""
def set_palette():
    pass

def set_style():
    pass

def set_size():
    pass

def draw_image():
    pass

def show_image():
    pass

def save_image():
    pass

def generate(config):
    set_style(config["style"])
    set_pallette(config["palette"])
    set_size(config["size"])