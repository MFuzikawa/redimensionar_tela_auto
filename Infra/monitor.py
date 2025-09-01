from screeninfo import get_monitors
from Domain import Monitor

def get_second_monitor():
    monitors = get_monitors()
    if len(monitors) < 2:
        print("[Infra] Apenas 1 monitor detectado.")
        return None
    second = monitors[1]
    return Monitor(second.x, second.y, second.width, second.height)
