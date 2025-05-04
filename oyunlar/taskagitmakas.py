import random

def tas_kagit_makas():
    secenekler = ["taş", "kağıt", "makas"]

    while True:
        bilgisayar = random.choice(secenekler)
        oyuncu = input("Taş, Kağıt veya Makas? (Çıkmak için q): ").lower()

        if oyuncu == "q":
            print("Oyun bitti!")
            break

        if oyuncu not in secenekler:
            print("Geçerli bir seçim yap!")
            continue

        print(f"Bilgisayarın seçimi: {bilgisayar}")

        if oyuncu == bilgisayar:
            print("Berabere!")
        elif (oyuncu == "taş" and bilgisayar == "makas") or \
             (oyuncu == "kağıt" and bilgisayar == "taş") or \
             (oyuncu == "makas" and bilgisayar == "kağıt"):
            print("Kazandın!")
        else:
            print("Kaybettin!")
