from classes.audio import Audio
from classes.chatBot import ChatBot
from screen.screenMain import ScreenMain
from screen.screenResult import ScreenResult

verifier = True

def funAudio():
    mic, verificador = Audio.recognizeAudio()
    print(mic)

    if verificador == True:
        print("audio capturado, aguarde a resposta!")
        return mic
    else:
        return None

while verifier:
    texto = ScreenMain.createScreen(fun=funAudio)
    print(texto)
    response = ChatBot.message(texto)
    verifier = ScreenResult.createScreen(response)

