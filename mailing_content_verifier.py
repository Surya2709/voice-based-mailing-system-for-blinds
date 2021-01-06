from stt_engine import get_audio
from tts_engine import speak
import utils
import smtp_hanlder
import os



#function to verify mail 
def verify_mail(text):
    speak(text)
    unverified = True
    cycle=True
    while unverified:

        if cycle:
            speak("please  say confirm to confirm  the reciever's mail : ")
            val_text=get_audio()
            
            if val_text == "confirm" or val_text=="confirmed":
                unverified=False
                return text
            cycle=False    
        else:
            loop=True 
            while loop:
                speak("please  type in the reciever's mail id :")
                new_text=input("Enter the mail id : ")
                speak(f"You have typed: {new_text} please  say confirm to proceed !")
                z=get_audio()
                if z== "confirm"or z=="confirmed":
                    loop == False
                    return new_text
                else: 
                    speak("please  try again !")
                
#function to verify subject
def verify_subject(text):
    speak(text)
    unverified = True
    cycle=True
    while unverified:

        if cycle:
            speak("please  say confirm to confirm  the subject : ")
            val_text=get_audio()
            
            if val_text == "confirm" or val_text=="confirmed":
                unverified=False
                return text
            cycle=False    
        else:
            loop=True 
            while loop:
                speak("please say the subject again ! :")
                new_text=get_audio()
                speak(f"You have said : {new_text} please  say confirm to proceed !")
                z=get_audio()
                if z== "confirm"or z=="confirmed":
                    loop == False
                    return new_text
                else: 
                    speak("please  try again !")
                    speak("please say the subject again")
                    text=get_audio()
                    verify_subject(text)
                



#fun to verify message
def verify_message(text):
    speak(text)
    unverified = True
    cycle=True
    while unverified:

        if cycle:
            speak("please  say confirm to confirm  the message : ")
            val_text=get_audio()
            
            if val_text == "confirm" or val_text=="confirmed":
                unverified=False
                return text
            cycle=False    
        else:
            loop=True 
            while loop:
                speak("please say the message again ! :")
                new_text=get_audio()
                speak(f"You have said : {new_text} please  say confirm to proceed !")
                z=get_audio()
                if z== "confirm"or z=="confirmed":
                    loop == False
                    return new_text
                else: 
                    speak("please  try again !")
                    speak("please say the message again")
                    text=get_audio()
                    verify_subject(text)
                
#verifying the file path
def verify_path(filename):
    if  os.path.isfile(filename):
        return filename
    else:
        uncorrect=True
        while uncorrect:
            speak("Please Enter the correct path!")
            speak("Please try again")
            fil = str(input("Enter the path again : "))
            if os.path.isfile(fil):
                speak(f"The path is {fil} , please confirm the path by saying okay !")
                s=get_audio()
                if s == "okay" or s== "ok":
                    return fil

            

