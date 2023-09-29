import speech_recognition as sr

class Audio:
    def recognizeAudio():
        
        rec = sr.Recognizer()

        try:
            #print(sr.Microphone().list_microphone_names())
            with sr.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic)
                print("Pode falar")
                audio = rec.listen(mic)
                texto = rec.recognize_google(audio, language="pt-BR")
        except:
            return 'Erro no microfone', False
        return texto, True
    #def speek(content):