def main_loop(chromedriver_path: str):
    monitor = get_second_monitor()
    if not monitor:
        return

    opera_manager = OperaManager(monitor)
    youtube_manager = YouTubeManager(chromedriver_path)

    print(f"[App] Monitor secundário: {monitor.width}x{monitor.height} @ ({monitor.x},{monitor.y})")

    # Espera até detectar um vídeo do YouTube
    print("[App] Procurando vídeo do YouTube no Opera GX...")
    video = None
    while not video:
        video = detect_youtube_video()
        time.sleep(2)
    print(f"[App] Vídeo detectado: {video.title}")
    youtube_manager.search_and_play_video(video)

    # Loop principal
    try:
        while True:
            # Reposicionar janelas do Opera
            for janela in opera_manager.get_opera_windows():
                opera_manager.reposition_window(janela)

            # Pular anúncios
            youtube_manager.skip_ads()

            time.sleep(2)

    except KeyboardInterrupt:
        print("[App] Interrompido pelo usuário.")
        youtube_manager.quit()
    except Exception as e:
        print(f"[App] Erro inesperado: {e}")
        youtube_manager.quit()


# ---------------------------- Entry ---------------------------- #
if __name__ == "__main__":
    CHROMEDRIVER_PATH = "chromedriver.exe" 
    main_loop(CHROMEDRIVER_PATH)