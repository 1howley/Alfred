from classes.audio import Audio
from classes.chatBot import ChatBot
from classes.browser import Browser
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

    splited = texto.split(' ')
    if splited[0] == 'tocar' or splited[0] == 'Tocar':
        x = 1
        query = ''        
        for x in range(len(splited)):
            query += ' ' + str(splited[x])
            
        print(query)
        Browser.process_youtube_video(query=query)
    else:
        response = ChatBot.message(texto)
        verifier = ScreenResult.createScreen(response)

