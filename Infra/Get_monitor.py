from screeninfo import get_monitors
from Domain.Monitor import Monitor
from typing import Optional

def get_second_monitor() -> Optional[Monitor]:
    monitors = get_monitors()
    if len(monitors) < 2:
        print("[Infra] Apenas 1 monitor detectado. São necessários 2 ou mais.")
        return None

    second = monitors[1]
    return Monitor(second.x, second.y, second.width, second.height)
