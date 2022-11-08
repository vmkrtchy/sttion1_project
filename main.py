# import tkinter as tk

# root = tk.Tk()

# temp_2 = f"This weekend I am going camping with {ProperNoun} {PersonsName}. I packed my lantern, sleeping bag, and {Noun}. I am so {Adjective} {Feeling} to {Verb} in a tent. I am {Adjective} {Feeling} 2 we might see an {Animal}, I hear theyre kind of dangerous. While we are camping, we are going to hike, fish, and {Verb2}. I have heard that the {Color} lake is great for { Verb} {ending in ing} . Then we will {Adverb} {ending in ly} hike through the forest for {Number} {Measure of Time}. If I see a {Color} {Animal} while hiking, I am going to bring it home as a pet! At night we will tell {Number} {Silly Word} stories and roast {Noun2} around the campfire!!"


temp_3 = "Dear {Proper Noun} {Persons Name}, I am writing to you from a {Adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {Color} {Animal} in {Place}. There are {Adjective2} {Magical Creature {Plural}} and {Adjective3} {Magical Creature {Plural}2} here! In the { Room in a House} there is a pool full of {Noun}. I fall asleep each night on a {Noun2} of {Noun{Plural}3} and dream of {Adjective4} { Noun {Plural}4}. It feels as though I have lived here for {Number} { Measureof time}. I hope one day you can visit, although the only way to get here now is {Verb {ending in ing}} on a {Adjective5} {Noun5}!!"

def temp_1():
    Number = input("Enter Number: ")
    Measureoftime = input("Enter Measure of time: ")
    Adjective = input("Enter Adjective: ")
    Adjective2 = input("Enter Adjective again: ")
    Noun = input("Enter Noun: ")
    Color = input("Enter color: ")
    PartoftheBody = input("Enter Part of the Body: ")
    Verb = input("Enter any Verb")
    Number2 = input("Enter Number: ")
    Noun2 = input("Enter Noun: ")
    Noun3 = input("Enter Noun: ")
    PartoftheBody2 = input("Enter Part of the Body: ")
    Noun4 = input("Enter Noun: ")
    Adjective3 = input("Enter Adjective again: ")
    SillyWord = input("Enter Silly Word")
    ModeofTransportation = input("Enter Modeof Transportation")


    temp_1 = f"It was about {Number} {Measureoftime} ago when I arrived at the hospital in a {ModeofTransportation}. The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {Noun} here. There are nurses here who have {Color} {PartoftheBody}. If someone wants to come into my room I told them that they have to {Verb} first. I’ve decorated my room with {Number2} {Noun2}. Today I talked to a doctor and they were wearing a {Noun3} on their {PartoftheBody2}. I heard that all doctors {Verb} {Noun4} every day for breakfast. The most { Adjective3} thing about being in the hospital is the {SillyWord} {Noun}!"

    print(temp_1)

choose_text = input("choose story")
if choose_text == "Hospital":
    temp_1()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# root.mainloop()
