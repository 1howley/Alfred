from playwright.sync_api import sync_playwright
import time

class Browser:

    def process_youtube_video(query):

        def convert_duration_to_seconds(duration):
            parts = duration.split(':')
            if len(parts) == 2:
                minutes, seconds = map(int, parts)
                total_seconds = minutes * 60 + seconds
                return total_seconds
            else:
                return None
            
        with sync_playwright() as p:
            global tempo
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            
            # Realiza a pesquisa no YouTube
            page.goto(f'https://www.youtube.com/results?search_query={query}')
            
            # Aguarda até que o primeiro vídeo da pesquisa esteja visível e, em seguida, clica nele
            try:
                page.wait_for_selector('ytd-video-renderer', state='visible', timeout=6000).click()
            except:
                print('Não foi possível acessar o primeiro vídeo da pesquisa')

            # Aguarda até que o botão "Pular anúncio" esteja visível e, em seguida, clica nele
            try:
                page.wait_for_selector('text=Pular Anúncios', state='visible', timeout=8000).click()
            except:
                print('Não foi possível pular o anúncio')

            # Aguarda até que o elemento da duração do vídeo esteja disponível e pega o valor
            time.sleep(5)

            try:
                duration = page.wait_for_selector('span.ytp-time-duration', state='visible', timeout=8000).text_content()
                print("Duração do vídeo:", duration)
                tempo = duration
            except:
                print('Não foi possível obter a duração do vídeo')
            
            sec = convert_duration_to_seconds(tempo)
            print(sec)
            
            time.sleep(sec)

            browser.close()

