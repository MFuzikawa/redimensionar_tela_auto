import pygetwindow as gw
import keyboard
from screeninfo import get_monitors
import time

def obter_config_segunda_tela():
    monitores = get_monitors()
    if len(monitores) < 2:
        print("Apenas 1 monitor detectado. O script requer 2 ou mais monitores.")
        return None

    segunda_tela = monitores[1]
    return {
        "x": segunda_tela.x,
        "y": segunda_tela.y,
        "width": segunda_tela.width,
        "height": segunda_tela.height
    }

def reposicionar_opera_segunda_tela(config_tela):
    janelas = gw.getWindowsWithTitle("Opera GX")
    if not janelas:
        return False

    janela = janelas[0]
    try:
        janela.activate()
        time.sleep(0.5)  

        janela.moveTo(config_tela["x"], config_tela["y"])
        janela.resizeTo(config_tela["width"], config_tela["height"])
        return True

    except Exception as e:
        print(f"Erro ao reposicionar a janela: {e}")
        return False

def monitorar_opera():
    config_tela = obter_config_segunda_tela()
    if not config_tela:
        return

    print(f"Segunda tela definida em {config_tela['width']}x{config_tela['height']} na posição ({config_tela['x']}, {config_tela['y']})")
    print("Monitorando a janela do Opera GX...")
    print("Pressione Ctrl+C no terminal para interromper.")

    try:
        while True:
            janelas = gw.getWindowsWithTitle("Opera GX")
            
            if janelas:
                janela = janelas[0]
                
                if (janela.left != config_tela["x"] or janela.top != config_tela["y"] or
                    janela.width != config_tela["width"] or janela.height != config_tela["height"]):
                    
                    print("Posição/tamanho do Opera GX foi alterado. Corrigindo...")
                    sucesso = reposicionar_opera_segunda_tela(config_tela)
                    if not sucesso:
                        print("Não foi possível corrigir. Tentando novamente...")
            
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    monitorar_opera()