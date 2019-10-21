import webbrowser
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

def dynamicmap(text):
    word_list= text.split()
    place=word_list[-1]
    i="https://www.google.com/maps/dir/Birla+Vishvakarma+Mahavidyalaya,+Mota+Bazaar,+Vallabh+Vidyanagar,+Anand,+Gujarat/"+place
    webbrowser.open(i,new=0)
    
def recording():
    import pyaudio
    import wave

    form_1 = pyaudio.paInt16 # 16-bit resolution
    chans = 1 # 1 channel
    samp_rate = 44100 # 44.1kHz sampling rate
    chunk = 4096 # 2^12 samples for buffer
    record_secs = 5 # seconds to record
    dev_index = 2 # device index found by p.get_device_info_by_index(ii)
    wav_output_filename = 'test1.wav' # name of .wav file

    audio = pyaudio.PyAudio() # create pyaudio instantiation

    # create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
    print("recording")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk, exception_on_overflow = False)
        frames.append(data)

    print("finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

def speech_to_text():
    import speech_recognition as sr
    file=("/home/pi/test1.wav")
    r = sr.Recognizer()

    with sr.AudioFile(file) as source:
        audio=r.record(source)

    try:
        speech = r.recognize_google(audio)
        speech = speech.lower()
        print("audio contains: ", speech)
        return speech

    except sr.UnknownValueError:
        print("Not understand")

    except sr.RequestError:
        print("no result")

def assistant():
    recording()
    sentence = speech_to_text()
    #if(sentence.count('sixth sense')>0):
    if(sentence.count("what's")>0 or sentence.count("how's")>0):
        if(sentence.count('weather')>0):
            print('The weather is sunny and its 42 degree celsius')
            os.system('xdg-open /home/pi/Desktop/weather.mp3')
        elif(sentence.count('josh')>0):
            print('high sir!')
    elif(sentence.count('call')>0):
        if(sentence.count('soham')>0):
            os.system('xdg-open /home/pi/callsoham.wav')
            i=40
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)
            time.sleep(3)
            GPIO.output(i,GPIO.HIGH)
        elif(sentence.count('mudit')>0):
            os.system('xdg-open /home/pi/callmudit.wav')
            i=38
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)
            time.sleep(3)
            GPIO.output(i,GPIO.HIGH)
        elif(sentence.count('chirag')>0):
            os.system('xdg-open /home/pi/callchirag.wav')
            i=37
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)
            time.sleep(3)
            GPIO.output(i,GPIO.HIGH)
    elif(sentence.count('take me')>0):
        if(sentence.count('baroda')):
            i="https://www.google.com/maps/dir/Anand,+Gujarat/Baroda,+Gujarat/@22.443404,72.9184879,11z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x395e4e7efd0c8885:0xa9a0b93c0c4b5215!2m2!1d72.928871!2d22.5645175!1m5!1m1!1s0x395fc8ab91a3ddab:0xac39d3bfe1473fb8!2m2!1d73.1812187!2d22.3071588"
            webbrowser.open(i,new=0)
        elif(sentence.count('surat')):
             i="https://www.google.com/maps/dir/Anand,+Gujarat/Surat,+Gujarat/@21.8745539,72.482799,9z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x395e4e7efd0c8885:0xa9a0b93c0c4b5215!2m2!1d72.928871!2d22.5645175!1m5!1m1!1s0x3be04e59411d1563:0xfe4558290938b042!2m2!1d72.8310607!2d21.1702401"
             webbrowser.open(i,new=0)
        elif(sentence.count('home')):
             i="https://www.google.com/maps/dir/Birla+Vishvakarma+Mahavidyalaya,+Mota+Bazaar,+Vallabh+Vidyanagar,+Anand,+Gujarat/Alkapuri+Society,+Sardargunj+Road,+Sardar+Ganj,+Anand,+Gujarat+388001,+India/@22.548508,72.9236848,14z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x395e4e74c03b7749:0xab364c66fd4834c!2m2!1d72.9238183!2d22.5525703!1m5!1m1!1s0x395e4c27d1c262f9:0x8a593f2048849097!2m2!1d72.9585475!2d22.5495507"
             webbrowser.open(i,new=0)
        else:
            dynamicmap(sentence)
    else:
        print('Sorry Could not get you')
        os.system('xdg-open /home/pi/Desktop/sorry.mp3')

#main() and code starts from here            
GPIO.setup(10,GPIO.IN)
while(1):
    if GPIO.input(10) == GPIO.HIGH:
        assistant()        
    

