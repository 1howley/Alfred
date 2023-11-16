from classes.audio import Audio
from classes.chatBot import ChatBot
from classes.browser import Browser
from classes.camera import Camera
from screen.screenMain import ScreenMain
from screen.screenResult import ScreenResult

verifier = True

def funAudio():
    mic, verificador = Audio.recognizeAudio()
    print('Audio capturado: ' + mic)

    if verificador == True:
        print("audio capturado, aguarde a resposta!")
        return mic
    else:
        return None
    
# Exemplo de uso
def display_result(result):
    if result:
        print('Rosto reconhecido!')
    else:
        print('Rosto não reconhecido!')

while verifier:
    texto, verifica = ScreenMain.createScreen(fun=funAudio)

    if verifica == True:
        if texto == None:
            Camera.recognize_face(result_callback=display_result)
        else:
            splited = texto.split(' ')
            if splited[0] == 'tocar' or splited[0] == 'Tocar':
                query = ''        
                for x in range(1, len(splited)):
                    query += str(splited[x]) + ' '
                    
                print(query)
                Browser.process_youtube_video(query=query)
            else:
                response = ChatBot.message(texto)
                verifier, text = ScreenResult.createScreen(response)
                while verifier == False:
                    text = ChatBot.message(text)
                    verifier, text = ScreenResult.createScreen(text)
    else:
        verifier = False
