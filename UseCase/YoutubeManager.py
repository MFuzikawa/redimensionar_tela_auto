from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

class YouTubeManager:
    def __init__(self, chromedriver_path):
        self.driver = None
        self.chromedriver_path = chromedriver_path

    def start_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--start-maximized")
        service = Service(self.chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def search_and_play_video(self, video):
        if self.driver is None:
            self.start_driver()
        query = video.title.replace(" ", "+")
        search_url = f"https://www.youtube.com/results?search_query={query}"
        self.driver.get(search_url)
        try:
            first_result = self.driver.find_element(By.ID, "video-title")
            first_result.click()
            print(f"[YouTubeManager] Vídeo '{video.title}' aberto.")
        except:
            print("[YouTubeManager] Não foi possível abrir o vídeo.")

    def skip_ads(self):
        if self.driver is None:
            return
        try:
            skip_button = self.driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button")
            skip_button.click()
            print("[YouTubeManager] Anúncio pulado!")
        except NoSuchElementException:
            pass

    def quit(self):
        if self.driver:
            self.driver.quit()
            print("[YouTubeManager] Driver encerrado.")
