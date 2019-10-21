import speech_recognition as sr
file=("/home/pi/test1.wav")
r = sr.Recognizer()

with sr.AudioFile(file) as source:
    audio=r.record(source)

try:
    speech = r.recognize_google(audio)
    print(speech)

except sr.UnknownValueError:
    print("Not understand") #reply

except sr.RequestError:
    print("no result") #reply
    

#def recognition(speech):
    #speech= speech.lower()
    #count = 1 
