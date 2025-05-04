import random

def adam_asmaca():
    kelimeler = ["python", "oyun", "bilgisayar", "programlama", "yapayzeka"]
    secilen = random.choice(kelimeler)
    gorunen = ["_"] * len(secilen)
    hak = 6

    while hak > 0 and "_" in gorunen:
        print("\nKelime:", " ".join(gorunen))
        tahmin = input("Harf tahmin et: ").lower()

        if tahmin in secilen:
            for i, harf in enumerate(secilen):
                if harf == tahmin:
                    gorunen[i] = tahmin
            print("Doğru!")
        else:
            hak -= 1
            print("Yanlış! Kalan hak:", hak)

    if "_" not in gorunen:
        print("Tebrikler! Kazandın! Kelime:", secilen)
    else:
        print("Kaybettin! Kelime:", secilen)
