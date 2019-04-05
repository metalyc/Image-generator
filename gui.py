from tkinter import *
import os
from palettes import p_list

styles = []
palettes = []
dimensions = ["width", "height"]

for i in p_list:
	palettes.append(i)

for root, dirs, files in os.walk("./styles/"):
	if "__pycache__" in dirs:
		dirs.remove("__pycache__")

	for f in files:
		if f.find('.py') > -1:
			styles.append(f[:-3])

def info():
	txt = "Image-generator is a tool for generating wallpapers with various designs."
	return txt

def palettes_options():
	txt = ["Select a palette:"]
	for p in range(len(palettes)):
		txt += [palettes[p]]

	txt += ["go back"]

	return txt

def styles_options():
	txt = ["Select a style:"]
	for s in range(len(styles)):
		txt += [styles[s]]

	txt += ["go back"]

	return txt

def sizes_options():
	txt = ["Change width or height:"]
	for d in range(len(dimensions)):
		txt += [dimensions[d]]

	txt += ["go back"]

	return txt

#main
root = Tk()
topFrame = Frame(root, padx=15, pady=15)
topFrame.pack()

w = Label(topFrame, text=info(), font=("Helvetica", 16), padx=45, pady=15).pack()

Label(topFrame, text=styles_options()[0], font=("Helvetica", 12), padx=45, pady=10).pack(anchor=W)
style = IntVar()
style.set(0)
styles_s = []
for s in range(len(styles)):
	r=Radiobutton(topFrame, text=styles[s], variable=style, value=s, padx=60)
	styles_s.append(r)
	r.pack(anchor=W)

Label(topFrame, text=palettes_options()[0], font=("Helvetica", 12), padx=45, pady=10).pack(anchor=W)
palette = IntVar()
palette.set(0)
palette_s = []
for p in range(len(palettes)):
	r=Radiobutton(topFrame, text=palettes[p], variable=palette, value=p, padx=60)
	palette_s.append(r)
	r.pack(anchor=W)

bottomFrame = Frame(topFrame, padx=45, width=600)
bottomFrame.pack(anchor=W)

entries = []
Label(bottomFrame, text="Size:", font=("Helvetica", 12), pady=10).pack(anchor=W)
for d in range(len(dimensions)):
	l = Label(bottomFrame, text=dimensions[d] + ":", font=("Helvetica", 10)).pack(anchor=W)
	x = Entry(bottomFrame)
	entries.append(x)
	x.pack(anchor=W)

warning = StringVar()
Label(bottomFrame, textvariable=warning, font=("Helvetica", 10)).pack(anchor=W)

def gen(x):
	i = entries[0].get()
	j = entries[1].get()

	if i == "" and j == "":
		i = '1920'
		j = '1080'
	else:
		for e in entries:
			try:
				if int(e.get()) < 2048 and int(e.get()) > 0:
					continue
				else:
					warning.set("Please enter valid image dimensions (1-2048px)")
					return -1
			except ValueError:
				warning.set("Please enter valid image dimensions (1-2048px)")
				return -1

	warning.set("")
	config = {
		"style": styles_s[style.get()].cget('text'),
		"palette": palette_s[palette.get()].cget('text'),
		"size": {
			"width": int(i),
			"height": int(j)
		}
	}

	from interface import generate
	generate(config)

generate_button = Button(topFrame, text="Generate Image!", bg="green", padx=5, pady=5)
generate_button.bind("<Button-1>", gen)
generate_button.pack()


root.mainloop()