from gtts import gTTS

tts = gTTS(text="The weather is sunny and its 42 degree celsius", lang='en')
tts.save("weather.wav")


