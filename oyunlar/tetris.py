import random

def tetris():
    bloklar = [
        ["####"],    # I
        ["##", "##"], # O
        ["###", " # "], # T
        ["## ", " ##"], # S
        [" ##", "## "]  # Z
    ]

    def yeni_blok():
        return random.choice(bloklar)

    print("Basit Tetris Simülasyonu - CTRL+C ile çıkış")
    try:
        while True:
            blok = yeni_blok()
            print("\nYeni Blok:")
            for satir in blok:
                print(satir)
            input("Devam etmek için Enter'a bas...")
    except KeyboardInterrupt:
        print("\nTetris Bitti!")
