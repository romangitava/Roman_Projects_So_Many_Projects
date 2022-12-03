# Welcome to ScreenTimer Project

import pyttsx3 # To download pyttsx3, start terminal and and write 'pip install pyttsx3'
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# This is speak function
def speak(audio):
    """
    This function is used to generate voice.
    """
    engine.say(audio)
    engine.runAndWait()

# This is to get localtime
def getDateTime():
    """
    This function is used to get localtime.
    """
    import time
    save_time = time.localtime()
    return time.strftime("Date: %d/%m/%y, Time: %H:%M", save_time)

# This is to save ScreenTimer
def save_screen_time(text):
    """
    This function is used to save ScreenTimer as a text.
    """
    with open('ScreenTimer.txt', 'w') as f:
        f.write(f'{getDateTime()} ----> {text}' + "\n")

# This function is get localtime tooo.
def getdate():
    """
    Why I made this function. You will think?
    I made this function becasue I have to compare date,
    Not time so that I can compare day to other day. Hence I made this function
    """
    import time
    tim = time.localtime()
    return time.strftime("%d%m%y", tim)

# This is reading (ScreenTimer.txt) so that I can get value and compare too.
with open('ScreenTimer.txt') as f3:
    store_vle = f3.read()

store_valuews = ""  # This is empty string. I made it for storing integers values.
for i in store_vle:
    if i.isdigit() == True:  # it returns numbers 
        store_valuews = store_valuews + i  # it stores the those numbers what it will return

values = store_valuews[10:]  #It return only time

sve_vle = store_valuews[:6] # It only returns date/month/year

date = getdate() # It stores <getdate()> function in a date variable 

if sve_vle == date:  # (ScreenTimer.txt) and <localtime> is equal

    if values == "": # If (ScreenTimer.txt) is a empty file
        typecast = 1   # then it will give 1
    else:
        typecast = int(values) # String into the integers typecasting
        typecast +=1  # 1 value is added Why I did that? You can check it without 1 increment. Explore it by yourself, you will know the reason

else: # otherwise return (it means other day)
    with open('DayTotalScreenTimer.txt', 'a') as r: # This is new .txt file
        r.write(store_vle + "\n" + "\n") # Append Screen timer into TotalScreenTimer.txt file
    typecast = 1 # Start your ScreenTimer from 1  

i = typecast
speak('ScreenTimer Project is activated')
while True:    
    time.sleep(60)
    if i == 1:
        save_screen_time(f'Your screen time is {i} minute')
        speak(f'{i} minute')
                
    else:     
        save_screen_time(f'Your screen time is {i} minutes') 
    i +=1   
