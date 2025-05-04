import math

def hesap_makinesi_menu():
    while True:
        print("\033[1;32;40m")
        print("╔═════════════════════╗")
        print("║    Hesap Makinesi   ║")
        print("║                     ║")
        print("║  1- Toplama         ║")
        print("║  2- Çarpma          ║")
        print("║  3- Çikarma         ║")
        print("║  4- Üst Alma        ║")
        print("║  5- Bölme           ║")
        print("║  6- Karekok Alma    ║")
        print("║  7- Ana Menüye Dön  ║")
        print("╚═════════════════════╝")

        secim = input("Seçiminiz: ")

        if secim == "1":
            a = float(input("Birinci sayi: "))
            b = float(input("İkinci sayi: ")) 
            print("Sonuç:", a + b)

        elif secim == "2":
            a = float(input("Birinci sayi: "))
            b = float(input("İkinci sayi: "))
            print("Sonuç:", a * b)

        elif secim == "3":
            a = float(input("Birinci sayi: "))
            b = float(input("İkinci sayi: "))
            print("Sonuç:", a - b)

        elif secim == "4":
            a = float(input("Taban: "))
            b = float(input("Üs: "))
            print("Sonuç:", a ** b)

        elif secim == "5":
            a = float(input("Bölünen sayi: "))
            b = float(input("Bölen sayi: "))
            if b == 0:
                print("Sifira bölme hatasi!")
            else:
                print("Sonuç:", a / b)

        elif secim == "6":
            a = float(input("Karekökü alinacak sayi: "))
            if a < 0:
                print("Negatif sayinin karekökü gerçek değil!")
            else:
                print("Sonuç:", math.sqrt(a))

        elif secim == "7":
            print("Ana menüye dönülüyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

        input("\nDevam etmek için Enter'a bas...")  
