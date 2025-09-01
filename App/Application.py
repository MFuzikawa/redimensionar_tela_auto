import time
from Infra.Get_monitor import get_second_monitor
from UseCase.OperaManager import OperaManager

def main():
    monitor = get_second_monitor()
    if not monitor:
        return

    opera_manager = OperaManager(monitor)

    print(f"[App] Segunda tela: {monitor.width}x{monitor.height} @ ({monitor.x},{monitor.y})")
    print("[App] Monitorando janelas do Opera GX...")
    print("[App] Pressione Ctrl+C para interromper.")

    try:
        while True:
            opera_windows = opera_manager.get_opera_windows()

            if opera_windows:
                for w in opera_windows:
                    success = opera_manager.reposition_window(w)
                    if success:
                        print(f"[App] Janela '{w.title}' ajustada com sucesso.")
                    else:
                        print(f"[App] Não foi possível ajustar a janela '{w.title}'.")
            else:
                print("[App] Nenhuma janela do Opera encontrada.")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\n[App] Script interrompido pelo usuário.")
    except Exception as e:
        print(f"[App] Erro inesperado: {e}")


if __name__ == "__main__":
    main()
