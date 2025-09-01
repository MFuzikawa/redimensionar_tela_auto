import pygetwindow as gw
from Domain.Monitor import Monitor

class OperaManager:

    def __init__(self, monitor: Monitor):
        self.monitor = monitor

    def get_opera_windows(self):
        return [w for w in gw.getAllWindows() if w.title and "Opera" in w.title]

    def reposition_window(self, window) -> bool:
        try:
            if window.isMinimized:
                window.restore()

            if (window.left == self.monitor.x and window.top == self.monitor.y and
                window.width == self.monitor.width and window.height == self.monitor.height):
                return True

            window.moveTo(self.monitor.x, self.monitor.y)
            window.resizeTo(self.monitor.width, self.monitor.height)
            return True
        except Exception as e:
            print(f"[UseCase] Erro ao reposicionar: {e}")
            return False
