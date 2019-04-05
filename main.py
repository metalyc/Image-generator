def info():
	txt = "Image-generator is a tool for generator wallpapers with various designs."
	return txt

#styles
styles = ["waves", "circles"]
palettes = ["Red on white", "Blue on white", "Green on white"]

#CLI options menus
def main_menu_options(style_picked = False, palette_picked = False):
	txt = ["You may customize the options shown here (defaults are random). Make a selection:"]
	
	if style_picked:
		txt += ["select style (" + style_picked + ")"]
	else:
		txt += ["select style"]

	if palette_picked:
		txt += ["select palette (" + palette_picked + ")"]
	else:
		txt += ["select palette"]

	txt += ["genereate image"]
	txt += ["exit"]

	return options_generator(txt)

def palettes_options():
	txt = ["Select a palette:"]
	txt += [palettes[0]]
	txt += [palettes[1]]
	txt += [palettes[2]]
	txt += ["Go back"]
	 
	return options_generator(txt)

def styles_options():
	txt = ["Select a style:"]
	txt += [styles[0]]
	txt += [styles[1]]
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
	return str([i for i in range(1, num)] + [0])

def get_user_input(prompt, options):
	prompt = ''.join(prompt)
	while True:
		i = input(prompt + "=>")
		if i in options:
			return i

#iscreens
def iscreen_styles(config):
	user_input = int( get_user_input(styles_options(), options(STYLE_OPTIONS)) )
	config["lastmenu"] = "styles"

	if user_input == 1:
		config["style"] = styles[user_input - 1]

	if user_input == 2:
		config["style"] = styles[user_input - 1]

	print("----- style selected:", config["style"], "-----")
	iscreen_main_menu(config)

def iscreen_palettes(config):
	user_input = int( get_user_input(palettes_options(), options(PALETTES_OPTIONS)) )
	config["lastmenu"] = "palettes"

	if user_input == 1:
		config["palette"] = palettes[user_input - 1]

	if user_input == 2:
		config["palette"] = palettes[user_input - 1]

	if user_input == 3:
		config["palette"] = palettes[user_input - 1]

	print("----- palette selected:", config["palette"], "-----")
	iscreen_main_menu(config)

def iscreen_main_menu(config = None):
	if config == None:
		user_input = int( get_user_input(main_menu_options(), options(MAIN_MENU_OPTIONS)) )
		config = { "style": "", "palette": "", "lastmenu": "main_menu" }
	else:
		style = palette = None
		if config["style"] != "":
			style = config["style"]

		if config["palette"] != "":
			palette = config["palette"]

		user_input = int( get_user_input(main_menu_options(style, palette), options(MAIN_MENU_OPTIONS)) )		

	if user_input == 1:
		iscreen_styles(config)

	if user_input == 2:
		iscreen_palettes(config)

	if user_input == 3:
		from interface import genereate
		generate(config)

	if user_input == 0:
		exit()

#options constants
MAIN_MENU_OPTIONS = len(main_menu_options()) - 1
STYLE_OPTIONS = len(styles_options()) - 1
PALETTES_OPTIONS = len(palettes_options()) - 1

print(info())
iscreen_main_menu()