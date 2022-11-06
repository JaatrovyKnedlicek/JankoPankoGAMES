import os
import sys
import time
#def
def incorrectOption():
    print("Incorrect option!")
    time.sleep(1)


def mainMenu():
    os.system("cls")
    print(" * KAKA ADVENTURES 1: HOME ALONE")
    print()
    print("1. Start new game")
    print("2. Credits")
    print("3. Exit")
    print()
    mainMenuAns=input("Select: ")
    if mainMenuAns=="1":
        start()
    elif mainMenuAns=="2":
        os.system("cls")
        print(" * CREDITS * ")
        print()
        print("Game maked by:")
        print("Džejno")
        print("Stories by:")
        print("tt: @kakavk42061420")
        print()
        input("Press any key to bak to menu...")
        mainMenu()
    elif mainMenuAns=="3":
        sys.exit()
    else:
        incorrectOption()
        mainMenu()

def cls():
    os.system("cls")

def start():
    cls()
    print("You are home alone")
    input("Press enter")
    dva()

def dva():
    cls()
    print("You are very bored") 
    print("1. Play games")
    print("2. Go outside")
    dvaAns=input("")
    if dvaAns=="1":
        tri()
    elif dvaAns=="2":
        sedem()
    else:
        incorrectOption()


def tri():
    cls()
    print("You decide to play on your Playstation")
    input("Press enter")
    styri()


def styri():
    cls()
    print("You suddenly hear a knock from your door")
    print("1. Open up")
    print("2. Continue")
    styriAns=input("")
    if styriAns=="1":
        jedenast()
    elif styriAns=="2":
        pet()
    else:
         incorrectOption()


def pet():
    cls()
    print("You play games until you suddenly get dragged into your game")
    input("Press enter")
    sest()


def sest():
    cls()
    print("You land in a desert")
    print("1. Find dhelter")
    print("2. Find food")
    sestAns=input("")
    if sestAns=="1":
        sestnast()
    elif sestAns=="2":
        dvanast()
    else:
         incorrectOption()

def sedem():
    cls()
    print("Youre now outside")
    print("1. Take a walk")
    print("2. Play football")
    sedemAns=input("")
    if sedemAns=="1":
        osem()
    elif sedemAns=="2":
        devet()
    else:
        incorrectOption()

def osem():
    cls()
    print("You see weird door")
    print("1. Enter")
    print("2. Keep walking")
    osemAns=input("")
    if osemAns=="1":
        sest()
    elif osemAns=="2":
        strnast()
    else:
        incorrectOption()
    

def devet():
    cls()
    print("You go to play football")
    input("Press enter")
    desat()

def desat():
    cls()
    print("After a while you get bored")
    print("1. Keep walking around")
    print("2. Go home")
    desatAns=input("")
    if desatAns=="1":
        strnast()
    elif desatAns=="2":
        dvadsat()
    else:
        incorrectOption()


def jedenast():
    cls()
    print(" * DEFEAT * ")
    print("Rake ending")
    print("It was a rake")
    input("Press any key to go to menu....")
    mainMenu()


def dvanast():
    cls()
    print("You spot camels")
    print("1. Go to them")
    print("2. Keep walking")
    dvanastAns=input("")
    if dvanastAns=="1":
        trinast()
    elif dvanastAns=="2":
        dvadsatdva()
    else:
        incorrectOption()
    

def trinast():
    cls()
    print("The camels had water")
    input("Press enter")
    sestnast()

def strnast():
    cls()
    print("You spot a bear")
    print("1. Run away")
    print("2. Play dead")
    strnastAns=input("")
    if strnastAns=="1":
        petnast()
    elif strnastAns=="2":
        devetnast()
    else:
        incorrectOption()

def petnast():
    cls()
    print(" * DEFEAT * ")
    print("Bear ending")
    print("The bear caught up to you and ate you :(")
    input("Press any key to go to menu....")
    mainMenu()

def sestnast():
    cls()
    print("You spot a village")
    print("1. Go to village")
    print("2. Keep walking")
    sestnastAns=input("")
    if sestnastAns=="1":
        sedemnast()
    elif sestnastAns=="2":
        dvadsatdva()

def sedemnast():
    cls()
    print("2 villagers asked you if you want to stay at their house.")
    print("Which one do you trust?")
    print("1. Villager 1")
    print("2. Villager 2")
    sedemnastAns=input("")
    if sedemnastAns=="1":
        osemnast()
    elif sedemnastAns=="2":
        dvadsattri()
    else:
         incorrectOption()


def osemnast():
    cls()
    print(" * DEFEAT * ")
    print("Trapped ending")
    input("Press any key to bak to menu...")
    mainMenu()

def devetnast():
    cls()
    print("After a while the bear loses interest in you")
    input("Press enter")
    dvadsat()
    

def dvadsat():
    cls()
    print("You go home")
    input("Press enter")
    dvadsatjedna()

def dvadsatjedna():
    cls()
    print("Do you play games now or go to sleep?")
    print("1. Play games")
    print("2. Sleep")
    dvadsatjednaAns=input("")
    if dvadsatjednaAns=="1":
        tri()
    elif dvadsatjednaAns=="2":
        dvadsatosem()
    else:
        incorrectOption()

def dvadsatdva():
    cls()
    print("You come across 2 paths")
    print("1. Left")
    print("2. Right")
    dvadsatdvaAns=input("")
    if dvadsatdvaAns == "1":
        dvadsatstyri()
    elif dvadsatdvaAns == "2":
        dvadsatpet()
    else:
        incorrectOption()


def dvadsattri():
    cls()
    print(" * VICTORY i guess * ")
    print("Cozy ending")
    print("Villager 2 was nice to you and give you food and place to be")
    input("Press any key to back to menu...")
    mainMenu()


def dvadsatstyri():
    cls()
    print("You spot a cave")
    print("1. Keep walking")
    print("2. Enter the cave")
    dvadsatstyriAns = input("")
    if dvadsatstyriAns == "1":
        dvadsatpet()
    elif dvadsatstyriAns == "2":
        dvadsatsest()
    else:
        incorrectOption()


def dvadsatpet():
    cls()
    print("You spot oasis")
    print("1. Go to oasis ")
    print("2. Keep waklking")
    dvadsatpetAns = input("")
    if dvadsatpetAns == "1":
        tridsat()
    elif dvadsatpetAns == "2":
        tridsattri()
    else: incorrectOption()

def dvadsatsest():
    cls()
    print("The cave is very narrow")
    input("Press enter")
    dvadsatsedem()

def dvadsatsedem():
    cls()
    print(" * DEFEAT * ")
    print("Cave ending :(")
    print("The cave was very narrow and you got stuck in ti")
    input("Press any key to back to menu...")
    mainMenu()


def dvadsatosem():
    cls()
    print("You go to sleep")
    input("Press enter")
    dvadsatdevet()

def dvadsatdevet():
    cls()
    print(" * VICTORY :))) * ")
    print("You woke up safetly in your house")
    input("Press any key to say good morning and back to menu...")
    mainMenu()


def tridsat():
    cls()
    print("You see a man at the oasis")
    input("Press enter")
    tridsatjedna()

def tridsatjedna():
    cls()
    print(" * VICTORY * ")
    print("Survivor ending")
    print("The man gave you a map and instructions on how to get home")
    input("Press any key to say thank you and back to home...")
    mainMenu()

def tridsatdva():
    cls()
    print("After walking for a while you hear noise from the sky")
    print("1. Check it out")
    print("2. Keep walking")
    tridsatdvaAns = input("")
    if tridsatdvaAns == "1":
        tridsattri()
    elif tridsatdvaAns == "2":
        tridsatstyri()
    else:
        incorrectOption()

def tridsattri():
    cls()
    print(" * VICTORY * ")
    print("Escape ending")
    print("It was a helicopter!")
    print("You waved at it and it came to save you")
    input("Press H as helicopter to safetly land and back to menu")
    mainMenu()


def tridsatstyri():
    cls()
    print("After a long time of walking you cant find any food and you have no water :(")
    input("Press enter")
    tridsatpet()

def tridsatpet():
    cls()
    print(" * DEFEAT * ")
    print("Starved ending")
    print("After a long trip without food you starved to death")
    input("Press any key to say its sad and back to menu")
    mainMenu()
    
#func
mainMenu()