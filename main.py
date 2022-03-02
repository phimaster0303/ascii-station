import pyfiglet
import art
import random
import os
os.system("cls")
print("What do you want to use?:")
print("[P]yfiglet | [A]rt")
asciitype = input("")


if asciitype.upper() == "P":
    fig = pyfiglet.Figlet()
    fonts = fig.getFonts()
    while True:
        rfont = random.choice(fonts)
        text = input("What text do you want to convert to ascii art?: ")
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