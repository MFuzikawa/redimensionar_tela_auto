import time
import os
import sys

from Infra import get_second_monitor
from Infra import detect_youtube_video
from UseCase import OperaManager
from UseCase import YouTubeManager

def main_loop(chromedriver_path):
    monitor = get_second_monitor()
    if not monitor:
        return

    opera_manager = OperaManager(monitor)
    youtube_manager = YouTubeManager(chromedriver_path)

    print(f"[App] Monitor secundário: {monitor.width}x{monitor.height} @ ({monitor.x},{monitor.y})")

    print("[App] Procurando vídeo do YouTube no Opera GX...")
    video = None
    while not video:
        video = detect_youtube_video()
        time.sleep(2)
    print(f"[App] Vídeo detectado: {video.title}")
    youtube_manager.search_and_play_video(video)

    try:
        while True:
            for janela in opera_manager.get_opera_windows():
                opera_manager.reposition_window(janela)
            youtube_manager.skip_ads()
            time.sleep(2)
    except KeyboardInterrupt:
        print("[App] Interrompido pelo usuário.")
        youtube_manager.quit()
    except Exception as e:
        print(f"[App] Erro inesperado: {e}")
        youtube_manager.quit()


if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        BASE_DIR = sys._MEIPASS
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    CHROMEDRIVER_PATH = os.path.join(BASE_DIR, "chromedriver.exe")
    main_loop(CHROMEDRIVER_PATH)
