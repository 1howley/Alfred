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
            
            page.goto(f'https://www.youtube.com/results?search_query={query}')
            
            try:
                page.wait_for_selector('ytd-video-renderer', state='visible', timeout=6000).click()
            except:
                print('Não foi possível acessar o primeiro vídeo da pesquisa')

            try:
                page.wait_for_selector('text=Pular Anúncios', state='visible', timeout=8000).click()
            except:
                print('Não foi possível pular o anúncio')

            time.sleep(8)

            try:
                duration = page.wait_for_selector('span.ytp-time-duration', state='visible', timeout=8000).text_content()
                print("Duração do vídeo:", duration)
                tempo = duration
            except:
                print('Não foi possível obter a duração do vídeo')
            
            
            sec = convert_duration_to_seconds(tempo)
            print(sec)

            timeout = time.time() + sec
            while True:
                if page.is_closed() or time.time() > timeout:
                    break
                time.sleep(1)
            
            browser.close()
            

            
