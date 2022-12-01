from colorama import init
from termcolor import colored
import time
import sys
import curses, time, os
from time import sleep
from pyfiglet import Figlet
import os

colors = ['yellow', 'red', 'green', 'blue']
f = Figlet(font="banner3-D",width = 200)
i = Figlet(font="doh",width = 200)
print (colored (f.renderText('Tumo labs'),'yellow'))

def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.09)

def temp3():
    ProperNoun         = input(colored("enter Proper Noun",'cyan'))
    PersonsName        = input(colored("enter Persons Name",'cyan'))
    Noun               = input(colored("enter Noun",'cyan'))
    Adjective          = input(colored("enter Adjective",'cyan'))
    Verb               = input(colored("Enter Verb",'cyan'))
    Adjective2         = input(colored("Enter Adjective",'cyan'))
    Animal             = input(colored("Enter Animal",'cyan'))
    Verb2              = input(colored("Enter verb (-ing)",'cyan'))
    Color              = input(colored("Enter color",'cyan'))
    Verbendingining    = input(colored("Enter verb (-ing)",'cyan'))
    Adverbeendinginly  = input(colored("Enter Adverb (-ing)",'cyan'))
    Number             = input(colored("Enter Number",'cyan'))
    MeasureofTime      = input(colored("Enter Measure of Time",'cyan'))
    Color2             = input(colored("Enter color",'cyan'))
    Animal2            = input(colored("Enter color",'cyan'))
    Number2            = input(colored("Enter number",'cyan'))
    SillyWord          = input(colored("Enter number",'cyan'))
    Noun2              = input(colored("Enter Noun",'cyan'))

    temp_3= f"This weekend I am going camping with {ProperNoun} {PersonsName}. I packed my lantern, sleeping bag, and {Noun}. I am so {Adjective} to {Verb} in a tent. I am {Adjective2} we might see an {Animal}, I hear theyre kind of dangerous. While we are camping, we are going to hike, fish, and {Verb2}. I have heard that the {Color} lake is great for { Verbendingining} . Then we will {Adverbeendinginly} hike through the forest for {Number} {MeasureofTime}. If I see a {Color2} {Animal2} while hiking, I am going to bring it home as a pet! At night we will tell {Number2} {SillyWord} stories and roast {Noun2} around the campfire!!"

    os.system('clear')
    print (colored (f.renderText('Tumo labs'),'yellow'))
    print (colored (i.renderText('Story 1'),'blue'))
    sys.stdout.write('                                               ')
    sp("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁\n\n")
    print(temp_3)










def temp2():
    PersonsName                 = input(colored("enter Persons Name",'cyan'))
    Adjective                   = input(colored("enter Adjective",'cyan'))
    Color                       = input(colored("enter Color",'cyan'))
    Animal                      = input(colored("enter Animal",'cyan'))
    Place                       = input(colored("enter Place",'cyan'))
    Adjective2                  = input(colored("enter Adjective",'cyan'))
    MagicalCreaturePlural       = input(colored("enter Magical Creature Plural",'cyan'))
    Adjective3                  = input(colored("enter Adjective",'cyan'))
    MagicalCreaturesPlural2     = input(colored("enter Magical Creatures Plural",'cyan'))
    RoominaHouse                = input(colored("enter Room in a House",'cyan'))
    Noun                        = input(colored("enter Noun",'cyan'))
    Noun2                       = input(colored("enter Noun",'cyan'))
    NounPlural                  = input(colored("enter Noun (plural)",'cyan'))
    Adjective4                  = input(colored("enter Adjective",'cyan'))
    NounPlural4                 = input(colored("enter Noun (Plural)",'cyan'))
    Number                      = input(colored("enter Number",'cyan'))
    Measureoftime               = input(colored("enter Measure of time",'cyan'))
    Verbendingining             = input(colored("enter Verb ending in -ing",'cyan'))
    Adjective5                  = input(colored("enter Adjective",'cyan'))
    Noun5                       = input(colored("enter Noun",'cyan'))
    NounPlural3 				= input(colored("Enter noun ",'cyan'))

    temp_2 = f" Dear {PersonsName}, I am writing to you from a {Adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {Color} {Animal} in {Place}. There are {Adjective2} {MagicalCreaturePlural} and {Adjective3} {MagicalCreaturesPlural2} here! In the {RoominaHouse} there is a pool full of {Noun}. I fall asleep each night on a {Noun2} of {NounPlural3} and dream of {Adjective4} {NounPlural4}. It feels as though I have lived here for {Number} { Measureoftime}. I hope one day you can visit, although the only way to get here now is {Verbendingining} on a {Adjective5} {Noun5}!!"

    os.system('clear')
    print (colored (f.renderText('Tumo labs'),'yellow'))
    print (colored (i.renderText('Story 2'),'blue'))
    sys.stdout.write('                                               ')
    sp("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁\n\n")

    print(temp_2)







def temp_1():
    Number = input(colored("Enter Number: ",'cyan'))
    Measureoftime = input(colored("Enter Measure of time: ",'cyan'))
    Adjective = input(colored("Enter Adjective: ",'cyan'))
    Adjective2 = input(colored("Enter Adjective again: ",'cyan'))
    Noun = input(colored("Enter Noun: ",'cyan'))
    Color = input(colored("Enter color: ",'cyan'))
    PartoftheBody = input(colored("Enter Part of the Body: ",'cyan'))
    VerNounPlural3b = input(colored("Enter any Verb",'cyan'))
    Number2 = input(colored("Enter Number: ",'cyan'))
    Noun2 = input(colored("Enter Noun: ",'cyan'))
    Noun3 = input(colored("Enter Noun: ",'cyan'))
    PartoftheBody2 = input(colored("Enter Part of the Body: ",'cyan'))
    Noun4 = input(colored("Enter Noun: ",'cyan'))
    Adjective3 = input(colored("Enter Adjective again: ",'cyan'))
    SillyWord = input(colored("Enter Silly Word",'cyan'))
    ModeofTransportation = input(colored("Enter Modeof Transportation",'cyan'))
    Verb  = input(colored("Enter Verb ",'cyan'))



    temp_1 = f"It was about {Number} {Measureoftime} ago when I arrived at the hospital in a {ModeofTransportation}. The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {Noun} here. There are nurses here who have {Color} {PartoftheBody}. If someone wants to come into my room I told them that they have to {Verb} first. I’ve decorated my room with {Number2} {Noun2}. Today I talked to a doctor and they were wearing a {Noun3} on their {PartoftheBody2}. I heard that all doctors {Verb} {Noun4} every day for breakfast. The most { Adjective3} thing about being in the hospital is the {SillyWord} {Noun}!"

    os.system('clear')
    print (colored (f.renderText('Tumo labs'),'yellow'))
    print (colored (i.renderText('Story 3'),'blue'))
    sys.stdout.write('                                               ')
    sp("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁\n\n")
    print(temp_1)


print (colored("Hi, dear user if you enter you can choose a b or c story but if you have story generated rundomly choose rundom",'green'))
choose_text = input("Enter your choice")

if choose_text == "a":
    temp_1()
elif choose_text == "b":
	temp3()
elif choose_text == "c":
    temp2()
elif choose_text == "random":
    import random
    a = ['a','b','c']
    res = random.choice(a)
    if res == "a":
        temp_1()
    if res == "b":
	    temp3()
    if res == "c":
        temp2()
else:
    print(colored('...:User it not volid option!', 'red'))


