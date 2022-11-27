# Day26 Snake Water Gun Game:)))

import random
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def s_w_g_gme():
    """
    This function is for Snake Water Gun Game
    """
    print("\n\t\t\t\tWelcome to Water Gun Game:)))))\n")
    speak("Welcome to Snake Water Gun Game:))")

    to_po_of_gme = ['S','W','G']
    speak("Press S for Snake, G for gun, W for water")
    print("\nPress---->\nS - Snake\nW - Water\nG - Gun\n")
    speak("Enter here")
    speak("You have only,10 chances, to be a winner")
    i = 0
    usr_scs = 0
    com_scs = 0
    gme_ovr = 0
    usr_un_key = 0
    while i < 10:
        
        com_inpt =  random.choice(to_po_of_gme)
        usr_inpt = input("Enter here: ")
        if usr_inpt.capitalize() == com_inpt:
            speak("Game Draw")
            print("\nGame Draw\n")
            gme_ovr +=1
            
        elif usr_inpt.capitalize() == "S"  and com_inpt == 'W':
            speak(f"Computer choosen{com_inpt}")
            speak("Congratulation, You won")
            print("\n🤗🤩😜You won😍😋🤑\n")
            usr_scs +=1
            
        elif usr_inpt.capitalize()=="W" and com_inpt == "S":
            speak(f"Computer choosen{com_inpt}")            
            speak("Sorry, Computer won")
            print("\nYou losed\n")
            com_scs +=1
            
        elif usr_inpt.capitalize() == "W" and com_inpt == "G":
            speak(f"Computer choosen{com_inpt}")
            speak("Congratulation, You won")
            print("\n🤗🤩😜You won😍😋🤑\n")
            usr_scs +=1
            
        elif usr_inpt.capitalize() =="G" and com_inpt == "W":
            speak(f"Computer choosen{com_inpt}")
            speak("Sorry, Computer won")
            print("\nYou losed\n")
            com_scs+=1
            
        elif usr_inpt.capitalize() == "G" and com_inpt == "S":
            speak(f"Computer choosen{com_inpt}")
            speak("Congratulation, You won")
            print("\n🤗🤩😜You won😍😋🤑\n")
            usr_scs +=1
            
        elif usr_inpt.capitalize() == "S" and com_inpt == "G":
            speak(f"Computer choosen{com_inpt}")
            speak("Sorry, Computer won")
            print("\nYou losed\n")
            com_scs +=1
        else:
            speak("You entered, unexpected keyword")
            print("\nYou entered unexpected keyword 😢😯\n")
            usr_un_key +=1
            
        i +=1 
    speak("The Game is End\nNow let's see your, and computer scores")
    speak(f"Computer scores is,{com_scs}")
    print("Computer scores:",com_scs)
    speak(f"your scores is,{usr_scs}")
    print("Your scores:", usr_scs)
    speak(f"and Game Over{gme_ovr} time")
    print("Game Draw:",gme_ovr)
    speak(f"{usr_un_key} time wrong input")
    print(f"{usr_un_key} time wrong input\n")
    speak("Now let's see, who is winner")
    if com_scs > usr_scs :
        print("\nThe final Decision--->>\n")
        speak("In this game, Computer is winner")
        print("\nComputer is winner\n")
    elif com_scs < usr_scs :
        print("\nThe final Decision--->>\n")
        speak("In this game, You are winner")
        print("\nYou are winner\n")
    else:
        speak("Game Draw, No one is winner")
        print("\nGame Draw, no one is winner\n")
s_w_g_gme()




