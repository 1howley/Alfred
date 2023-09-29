from classes.audio import Audio
from classes.chatBot import ChatBot
from screen.screenMain import ScreenMain
from screen.screenResult import ScreenResult

def funAudio():
    mic, verificador = Audio.recognizeAudio()
    print(mic)

    if verificador == True:
        print("foi")#(ChatBot.message(mic))
        return mic
    else:
        print(mic)
        return None

texto = ScreenMain.createScreen(fun=funAudio)
print(texto)

