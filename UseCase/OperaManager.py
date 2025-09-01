import pygetwindow as gw

class OperaManager:
    def __init__(self, monitor):
        self.monitor = monitor

    def get_opera_windows(self):
        return [janela for janela in gw.getAllWindows() if janela.title and "Opera" in janela.title]

    def reposition_window(self, janela):
        try:
            if janela.isMinimized:
                janela.restore()
            if (janela.left == self.monitor.x and janela.top == self.monitor.y and
                janela.width == self.monitor.width and janela.height == self.monitor.height):
                return True
            janela.moveTo(self.monitor.x, self.monitor.y)
            janela.resizeTo(self.monitor.width, self.monitor.height)
            return True
        except Exception as e:
            print(f"[OperaManager] Erro: {e}")
            return False