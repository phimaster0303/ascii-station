import pyfiglet, art, simple_chalk as chalk, random, os
chalk.black(os.system("cls"))
chalk.black(os.system("pip install pyfiglet"))
chalk.black(os.system("cls"))
chalk.black(os.system("pip install art"))
chalk.black(os.system("cls"))
chalk.black(os.system("pip install simple_chalk"))
chalk.black(os.system("cls"))
chalk.black(os.system("pip install os"))
chalk.black(os.system("cls"))
#Ask what text2ascii libary you want to use
print(chalk.blueBright("What do you want to use?:"))
print((chalk.green("[P]yfiglet ")+ chalk.blue("|") + chalk.red(" [A]rt")))
asciitype = input("")


if asciitype.upper() == "P":
    fig = pyfiglet.Figlet()
    fonts = fig.getFonts()
    while True:
        rfont = random.choice(fonts)
        text = input(chalk.magenta("What text do you want to convert to ascii art?: "))
        print(pyfiglet.figlet_format(text,font=rfont))
        print(rfont)
elif asciitype.upper() == "A":
    print("What size do you want the ascii art to be? | 1 -> small | 2 -> medium | 3 -> large | 4 -> X-large")
    asciisize = input()
    while True:
        if asciisize == "1":
            asciitext = input("What text do you want to convert to ascii art?: ")
            art.tprint(asciitext, font="random-small")
        elif asciisize == "2":
            asciitext = input("What text do you want to convert to ascii art?: ")
            art.tprint(asciitext, font="random-medium")
        elif asciisize == "3":
            asciitext = input("What text do you want to convert to ascii art?: ")
            art.tprint(asciitext, font="large")
        elif asciisize == "4":
            asciitext = input("What text do you want to convert to ascii art?: ")
            art.tprint(asciitext, font="random-xlarge")