import pygetwindow as gw
import keyboard
from screeninfo import get_monitors
import time 

def fixar_opera_segunda_tela():

    monitores = get_monitors()
    if len(monitores) < 2:
        print("Só foi detectado 1 monitor.")
        return None, None, None
    
    segunda_tela = monitores[1]
    alvo_x, alvo_y = segunda_tela.x, segunda_tela.y; 
    alvo_w, alvo_h = segunda_tela.width, segunda_tela.height

    return alvo_x, alvo_y, alvo_w, alvo_h

def reposicionar_opera(x ,y , w , h):
    janelas = gw.getWindowsWithTitle("Opera GX")
    if not janelas:
        return False
    
    janela = janelas[0]
    try:
        janela.activate()
        time.sleep(0.2)

        janela.moveTo(x, y)
        janela.resizeTo(w, h)

        keyboard.press_and_release("f11")

    except Exception as e:
        print("Error", e)
        return False
    

def monitorar_opera():
    x, y, w, h = fixar_opera_segunda_tela()
    if not x:
        return
    
    print(f"Segunda tela definida em{w}x{h} posição ({x}, {y})")
    while True:
        janelas = gw.getWindowsWithTitle("Opera GX")
        if janelas:
            janela = janelas[0]

            if (janela.left != x or janela.top != y or
                janela.width != w or janela.height != h):
                print("Corrigindo posição do Opera GX...")
                reposicionar_opera(x, y, w, h)



if __name__ == "__main__":
    monitorar_opera()
