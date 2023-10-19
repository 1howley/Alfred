from playwright.sync_api import sync_playwright

class Browser:
    def query(link, query):
        with sync_playwright() as pw:
            nav = pw.chromium.launch(headless=False)
            pag = nav.new_page()
            pag.goto(link + query)            


Browser.query('https://www.youtube.com/results?search_query=', 'lugarmaisfriodomundo')