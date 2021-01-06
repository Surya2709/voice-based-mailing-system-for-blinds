import speech_recognition as sr
import os



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Processing .....")

        said = ""

        try:
            said = r.recognize_google(audio)
            print(f"you said : {said}")
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()
