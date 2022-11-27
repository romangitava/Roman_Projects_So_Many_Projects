import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class Reminder_ME:
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def getdate():
        import time 
        get_date = time.localtime()
        return time.strftime("Time is %M  minutes, past %H", get_date)
      

    def gettime():
        import time 
        get_time = time.localtime()
        return time.strftime("%H:%M", get_time)

    def save_datetime():
        import time
        save_datetime = time.localtime()
        return time.strftime("Date ---> %d/%m/%y, Time ---> %H:%M:%S", save_datetime)

    print(getdate())
    import time
    speak('I am activated')
    speak('My name is kety Perry\n you can use me as a reminder\n to use me, firstly you have to set time')
    speak('Enter hours here')

    while True:
        try:
            usr_set_hour = int(input('\n\t\t\t\tEnter Time Here\nEnter hour: '))
            speak('Enter minutes here')
            usr_set_minutes = int(input('Enter minutes: '))
            user_set_hour_typecast = str(usr_set_hour)
            user_set_minutes_typecast = str(usr_set_minutes)

            # Condition during setting time

            if len(user_set_hour_typecast) == 1:
                add_zero_in_hour = '0' + user_set_hour_typecast   
                user_set_hour_typecast = add_zero_in_hour

            if len(user_set_minutes_typecast) == 1:
                add_zero_in_minutes = '0' + user_set_minutes_typecast
                user_set_minutes_typecast = add_zero_in_minutes 
                        
            if len(user_set_hour_typecast) > 2:
                speak('Sorry, You entered invalid time\n Please Try again')
                print('You set invalid time')
                continue
            if len(user_set_minutes_typecast) > 2:
                speak('Sorry, You entered invalid minutes\n Please try again')    
                print('You set invalid time')
                continue
            else:
                break
            
        except Exception:
            speak('Sorry,You entered unexpected keyword\n Please Try again')
            print('You can only numbers')
            continue
    usr_get_spoken = input('\nEnter here what you want to me speak: ')
    with open('Set_Command_To_Speak.txt', 'a') as f:
        f.write(save_datetime() +" "+ usr_get_spoken + "\n")

    now_ready_time = user_set_hour_typecast + ':' + user_set_minutes_typecast
    
    print(now_ready_time)
    print(type(now_ready_time))
    while True:
        time.sleep(1)
        if gettime() == now_ready_time:
            print('Hello')
            speak(usr_get_spoken)
            break
        elif gettime() > now_ready_time:
            print('Bye')
            speak(f'User, You had set {usr_set_minutes} minutes, past {usr_set_hour} \n but at this moment {getdate()} \n so you are late')
            break
    
    
    
    
