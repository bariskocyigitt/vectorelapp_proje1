import random

def mayin_tarlasi():
    boyut = 5
    mayin_x = random.randint(0, boyut-1)
    mayin_y = random.randint(0, boyut-1)

    print(f"{boyut}x{boyut} alanda bir mayın var. Hücre seç!")

    while True:
        try:
            x = int(input(f"Satır (0-{boyut-1}): "))
            y = int(input(f"Sütun (0-{boyut-1}): "))

            if x == mayin_x and y == mayin_y:
                print("BOOM! Mayına bastın! Oyun Bitti.")
                break
            else:
                print("Güvenli! Devam edebilirsin.")
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")
