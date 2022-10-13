#VivaVoice3 Modules Import
import modules.time

#Pip modules Import
import speech_recognition as sr

#Modules dictionary


# speechRegonition
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

understood = r.recognize_google(audio)
