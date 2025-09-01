import pygetwindow as gw
from Domain import Video

def detect_youtube_video():
    youtube_windows = [janela for janela in gw.getAllWindows() if janela.title and "YouTube" in janela.title]
    if not youtube_windows:
        return None
    title = youtube_windows[0].title.replace(" - YouTube", "")
    return Video(title)
