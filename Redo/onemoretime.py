class pallettes:
    list = [
        {
        'name' : 'Red on white',
        'value' : ((255, 255, 255), (244, 66, 53))
        },
        {
        'name' : 'Blue on white',
        'value' : ((255, 255, 255), (66, 53, 244))
        },
        {
        'name' : 'Green on white',
        'value' : ((255, 255, 255), (53, 244, 66))
        }
        ]
    def select():
        global pallette
        while True:
            print("Select a pallette:")
            options = []
            for i, v in enumerate(pallettes.list):
                print(str(i + 1) + '.\t' + v['name'])
                options.append(i)
            print("0.\tGo back")
            a = input("Selection: ")
            try:
                if int(a) - 1 in options:   # FIXME: int in index of list
                    pallette = palletes.list[a]
                    break
                elif a == '0':
                    return mainmenu()
                else:
                    print("Selection not recognized")
            except:
                print("Selection not recognized")

class styles:
    list = [wave, cirlces]
    def select():
        global style
        while True:
            print("Select a style:")
            options = []
            for i, v in enumerate(styles.list):
                print(str(i+1) + '.\t' + v)
                options.append(i)
            print("0.\tGo back")
            a = input("Selection: ")
            try:
                if int(a) - 1 in options:   # FIXME: int in index of list
                    style = style.list[a]
                    break
                elif a == '0':
                    return mainmenu()
                else:
                    print("Selection not recognized")
            except:
                print("Selection not recognized")
    def wave(): # FIXME: add code
        pass
    def cirlces(): # FIXME: add code
        pass

class sizes:
    list = [ # FIXME: make some stuff
        {
        'name' : '1920x1080',
        'value' : (1920, 1080)
        }
    ]
    def select():
        global size
        while True:
            print("Select a Size:")
            options = []
            for i, v in enumerate(sizes.list):
                print(str(i+1) + '.\t' + v['name'])
                options.append(i)
            print("0.\tGo back")
            a = input("Selection: ")
            try:
                if int(a) - 1 in options:   # FIXME: int in index of list
                    size = sizes.list[a]
                    break
                elif a == '0':
                    return mainmenu()
                else:
                    print("Selection not recognized")
            except:
                print("Selection not recognized")
