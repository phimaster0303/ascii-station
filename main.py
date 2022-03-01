import pyfiglet, art, simple_chalk as chalk, random


#Ask what text2ascii libary you want to use
print("What do you want to use?:")
print((chalk.green("[P]yfiglet ")+ chalk.blue("|") + chalk.red(" [A]rt")))
asciitype = input("")


if asciitype.upper() == "P":
    randomfont = input("Do you want to use a random font? [Y]es | [N]o: ")
    if randomfont.upper() == "Y":
        fig = pyfiglet.Figlet()
        fonts = fig.getFonts()
        while True:
            rfont = random.choice(fonts)
            text = input("What text do you want to convert to ascii art?: ")
            print(pyfiglet.figlet_format(text,font=rfont))
            print(rfont)
    else:
        while True:
            ifont = input("What font do you want to use: ")
            itext = input("What text do you want to convert to ascii art: ")
            pyfiglet.figlet_format(itext, font=ifont)
elif asciitype.upper() == "A":
    print("What size do you want the ascii art to be? | 1 -> small | 2 -> medium | 3 -> large | 4 -> X-large")
    asciisize = input()
    while True:
        match asciisize:
            case "1":
                asciitext = input("What text do you want to convert to ascii art?: ")
                art.tprint(asciitext, font="random-small")
            case "2":
                asciitext = input("What text do you want to convert to ascii art?: ")
                art.tprint(asciitext, font="random-medium")
            case "3":
                asciitext = input("What text do you want to convert to ascii art?: ")
                art.tprint(asciitext, font="large")
            case "4":
                asciitext = input("What text do you want to convert to ascii art?: ")
                art.tprint(asciitext, font="random-xlarge")