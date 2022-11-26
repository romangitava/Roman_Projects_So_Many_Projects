import pyttsx3
import time
from pygame import mixer
from plyer import notification
import random
engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def noti(tl, mess):
    notification.notify(
        title = tl,
        message = mess,
        timeout = 10
    )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getdate():
    import time
    get_time = time.localtime()
    return time.strftime('Date: %d/%m/%y, Time: %H:%M:%S', get_time)

def time_tell():
    import time
    name_tuple = time.localtime()
    return time.strftime("Roman, Time is %M  minutes, past %H", name_tuple)

def musiconloop(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

def save_txt(text):
    with open('Pomodoro.txt', 'a') as f:
        f.write(f'DateTime: {str([str(getdate())])}, ---->  {text}' + "\n")


def pomo_pro(n):
    speak('Pomodoro technique project is activited')

        
    while True:
        print(n)
        time.sleep(60)        
        n +=1
        if n % 100 == 0 :
            speak(f'{time_tell()}')
            speak(f'Roman you have been studying {n} minutes \n I think, You should take a long term break\n That must be 20 minutes\n Here\'s your reminder, Till then roman\n Enjoy to yourself')
            noti('Have a long term break', f'Hello Roman, I am lucy. You have been studying for {n} minutes. I think, You must take a long term break. That must be 20 minutes Till then, Enjoy to Yourself')
            save_txt(f'Roman, You have been studied {n} minutes')
            j = 0
            while j < 21:
                print(j)
                time.sleep(60)
                j +=1
                if j == 20:
                    speak(f'{time_tell()}')
                    speak('Roman, Time has been over. Get back to the work')
                    noti('Reminder To get back to the work', 'Roman Now your time was over and now you have to get back to the work.')
                    save_txt('Roman, You took 20 minutes break')
                    break

                    
        else:
            if n % 75 == 0:
                speak(f'{time_tell()}')
                speak(f"Roman you have been studying {n} minutes \n I think, You should take a 5 minutes break\n Here's your reminder, Till then roman\n Enjoy to the music")
            # print(n)
                noti('Have a little break', f'Hello Roman, I am lucy. You have been studying for {n} minutes. I think,You should take a litle break')
                save_txt(f'Roman, You have been studied {n} minutes')
                l = ['Punjabi.mp3','Jayy.mp3','Guri.mp3','Koshish.mp3', 'Bingo.mp3', 'Mehnat.mp3', 'Amanta.mp3', 'Tere_Karke.mp3', 'Phulkari.mp3', 'Sabr.mp3', 'Lab.mp3']
                rand = random.choice(l)
                musiconloop(rand)
                i = 0
                while i < 6:
                    # print(i)
                    time.sleep(60)
                    i +=1
                    if i == 5:
                        mixer.music.stop()
                        speak(f'{time_tell()}')
                        speak('Roman, Time has been over. Get back to the work')
                        noti('Reminder To get back to the work', 'Roman Now your time was over and now you have to get back to the work.')
                        save_txt('Roman, You took 5 minutes break')
                        break 

                
            elif n % 50 == 0:
                speak(f'{time_tell()}')
                speak(f"Roman you have been studying {n} minutes \n I think, You should take a 5 minutes break\n Here's your reminder, Till then roman\n Enjoy to the music")
            # print(n)
                noti('Have a little break', f'Hello Roman, I am lucy. You have been studying for {n} minutes. I think,You should take a litle break')
                save_txt(f'Roman, You have been studied {n} minutes')
                l = ['Punjabi.mp3','Jayy.mp3','Guri.mp3','Koshish.mp3', 'Bingo.mp3', 'Mehnat.mp3', 'Amanta.mp3', 'Tere_Karke.mp3', 'Phulkari.mp3', 'Sabr.mp3', 'Lab.mp3']
                rand = random.choice(l)
                musiconloop(rand)
                i = 0
                while i < 6:
                    # print(i)
                    time.sleep(60)
                    i +=1
                    if i == 5:
                        mixer.music.stop()
                        speak(f'{time_tell()}')
                        speak('Roman, Time has been over. Get back to the work')
                        noti('Reminder To get back to the work', 'Roman Now your time was over and now you have to get back to the work.')
                        save_txt('Roman, You took 5 minutes break')
                        break 
            elif n % 25 == 0:
                speak(f'{time_tell()}')
                speak(f"Roman you have been studying {n} minutes \n I think, You should take a 5 minutes break\n Here's your reminder, Till then roman\n Enjoy to the music")
            # print(n)
                noti('Have a little break', f'Hello Roman, I am lucy. You have been studying for {n} minutes. I think,You should take a litle break')
                save_txt(f'Roman, You have been studied {n} minutes')
                l = ['Punjabi.mp3','Jayy.mp3','Guri.mp3','Koshish.mp3', 'Bingo.mp3', 'Mehnat.mp3', 'Amanta.mp3', 'Tere_Karke.mp3', 'Phulkari.mp3', 'Sabr.mp3', 'Lab.mp3']
                rand = random.choice(l)
                musiconloop(rand)
                                
                i = 0
                while i < 6:
                    # print(i)
                    time.sleep(60)
                    i +=1
                    if i == 5:
                        mixer.music.stop()
                        speak(f'{time_tell()}')
                        speak('Roman, Time has been over. Get back to the work')
                        noti('Reminder To get back to the work', 'Roman Now your time was over and now you have to get back to the work.')
                        save_txt('Roman, You took 5 minutes break')
                        break      
            

                
            
              

pomo_pro(0)
        
