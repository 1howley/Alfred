from classes.audio import Audio
from classes.chatBot import ChatBot
from screen.screenMain import ScreenMain
from screen.screenResult import ScreenResult
from screen.screenRecording import ScreenRecording
import threading

def fun():
    mic, verificador = Audio.recognizeAudio()
    print(mic)

    if verificador == True:
        print("foi")#(ChatBot.message(mic))
    else:
        print(mic)

ScreenMain.createScreen()

t2 = threading.Thread(target=ScreenRecording.createScreen)
t1 = threading.Thread(target=fun)
t1.start()
t2.start()
