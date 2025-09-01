import pygetwindow as gw
from screeninfo import get_monitors
import time
import platform

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

def reposicionar_janela(janela, config_tela):
    try:
        if janela.isMinimized:
            janela.restore()  

        if (janela.left == config_tela["x"] and janela.top == config_tela["y"] and
            janela.width == config_tela["width"] and janela.height == config_tela["height"]):
            return True 

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
    print("Monitorando as janelas do Opera GX...")
    print("Interrompa no gerenciador de tarefas.")

    try:
        while True:
            janelas_opera = []
            for janela in gw.getAllWindows():
                if janela.title and "Opera" in janela.title:
                    janelas_opera.append(janela)
                elif platform.system() == "Windows" and janela._hWnd:

                    class_name = gw._getWindowClassName(janela._hWnd)
                    if class_name and "Opera" in class_name:
                        janelas_opera = [janela for janela in gw.getAllWindows() if janela.title and "Opera" in janela.title]

            if janelas_opera:
                for janela in janelas_opera:
                    sucesso = reposicionar_janela(janela, config_tela)
                    if sucesso:
                        print(f"Janela '{janela.title}' ajustada com sucesso.")
                    else:
                        print(f"Não foi possível ajustar a janela '{janela.title}'.")
            else:
                print("Nenhuma janela do Opera encontrada.")

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    monitorar_opera()
