DEFAULT_WIDTH = 1920
DEFAULT_HEIGHT = 1080

def info():
	txt = "Image-generator is a tool for generator wallpapers with various designs."
	return txt

#styles
styles = ["waves", "circles"]
palettes = ["Red on white", "Blue on white", "Green on white", "Violet on white", "Orange on white", "Red on dark", "Blue on dark", "Green on dark", "Violet on dark", "Orange on dark"]
dimensions = ["width", "height"]

#CLI options menus
def main_menu_options(style_picked, palette_picked, size_picked):
	txt = ["You may customize the options shown here (defaults will be used otherwise). Make a selection:"]

	if style_picked != "":
		txt += ["select style (" + style_picked + ")"]
	else:
		txt += ["select style"]

	if palette_picked != "":
		txt += ["select palette (" + palette_picked + ")"]
	else:
		txt += ["select palette"]

	txt += ["image size (" + str(size_picked["width"]) + "x" + str(size_picked["height"]) + ")"]
	txt += ["genereate image"]
	txt += ["exit"]

	return options_generator(txt)

def palettes_options():
	txt = ["Select a palette:"]
	for p in range(len(palettes)):
		txt += [palettes[p]]

	txt += ["go back"]

	return options_generator(txt)

def styles_options():
	txt = ["Select a style:"]
	for s in range(len(styles)):
		txt += [styles[s]]

	txt += ["go back"]

	return options_generator(txt)

def sizes_options():
	txt = ["Change width or height:"]
	for d in range(len(dimensions)):
		txt += [dimensions[d]]

	txt += ["go back"]

	return options_generator(txt)

#other functions
def options_generator(txt):
	for t in range(len(txt)):
		txt[t] = txt[t] + '\n'
		if t == 0:
			continue

		if t == len(txt) - 1:
			txt[t] = "0.\t" + txt[t]
			continue

		txt[t] = str(t) + ".\t" + txt[t]

	return txt

def options(num):
	return [str(i) for i in range(1, num)] + ['0']

def get_user_input(prompt, options, invalid = None):
	prompt = ''.join(prompt)
	while True:
		i = input(prompt + "=>")
		if i != "" and i in options:
			return i
		else:
			if invalid == None:
				invalid = 'please enter a valid input'

			print(invalid)

#iscreens
def iscreen_styles(config):
	prompt = styles_options()
	valid_options = options(len(prompt) - 1)
	user_input = int( get_user_input(prompt, valid_options))

	for vo in valid_options:
		if user_input == int(vo):
			config["style"] = styles[user_input - 1]
			break

	print("----- style selected:", config["style"], "-----")
	iscreen_main_menu(config)

def iscreen_palettes(config):
	prompt = palettes_options()
	valid_options = options(len(prompt) - 1)
	user_input = int( get_user_input(prompt, valid_options))

	for vo in valid_options:
		if user_input == int(vo):
			config["palette"] = palettes[user_input - 1]
			break

	print("----- palette selected:", config["palette"], "-----")
	iscreen_main_menu(config)

def iscreen_sizes(config):
	prompt = sizes_options()
	user_input = int( get_user_input(prompt, options(len(prompt) - 1)) )

	if user_input == 1:
		config["size"]["width"] = get_user_input("Enter cutsom width:", options(2048))
		print("----- custom size selected: (", str(config["size"]["width"]) + "x" + str(config["size"]["height"]) + ")", "-----")
		iscreen_sizes(config)

	if user_input == 2:
		config["size"]["height"] = get_user_input("Enter cutsom height:", options(2048))
		print("----- custom size selected: (", str(config["size"]["width"]) + "x" + str(config["size"]["height"]) + ")", "-----")
		iscreen_sizes(config)

	iscreen_main_menu(config)

def iscreen_main_menu(config = None):
	user_input = None
	if config == None:
		config = {
			"style": "",
			"palette": "",
				"size": {
					"width": DEFAULT_WIDTH,
					"height": DEFAULT_HEIGHT
				}
			}
	else:
		style = palette = size = None
		if config["style"] != "":
			style = config["style"]

		if config["palette"] != "":
			palette = config["palette"]

		if config["size"]["width"] != DEFAULT_WIDTH and config["size"]["height"] != DEFAULT_HEIGHT:
			size = config["size"]

	prompt = main_menu_options(config["style"], config["palette"], config["size"])
	user_input = int( get_user_input(prompt, options(len(prompt) - 1)) )

	if user_input == 1:
		iscreen_styles(config)

	if user_input == 2:
		iscreen_palettes(config)

	if user_input == 3:
		iscreen_sizes(config)

	if user_input == 4:
		if config["style"] == "":
			config["style"] = styles[0]

		if config["palette"] == "":
			config["palette"] = palettes[0]

		from interface import generate
		generate(config)
		print("yay")
		exit()

	if user_input == 0:
		exit()

print(info())
iscreen_main_menu()
