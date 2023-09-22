from classes.audio import Audio
from classes.chatBot import ChatBot

mic, verificador = Audio.recognizeAudio()
print(mic)

if verificador == True:
    print(ChatBot.message(mic))
else:
    print(mic)