from hesapmakinesi import hesapmakinesi_menu
from oyunlar import oyunlar_menu
from dovizkuru import dovizkuru_menu

def main_menu():
    while True:
        print("\033[1;32;40m")
        print("╔═════════════════════╗")
        print("║     VEKTOREL APP    ║")
        print("║                     ║")
        print("║  1- Hesap Makinesi  ║")
        print("║  2- Oyunlar         ║")
        print("║  3- Doviz Kuru      ║")
        print("║  4- Hava Durumu     ║")
        print("║  5- Cikis           ║")
        print("║                     ║")
        print("║   Seçiminiz nedir?  ║")
        print("╚═════════════════════╝")

        secim = input("Seçiminiz: ")
        
        if secim == "1":
            hesapmakinesi_menu.hesap_makinesi_menu()
        elif secim == "2":
            oyunlar_menu.oyunlar_menu()
        elif secim == "3":
            dovizkuru_menu.dovizkuru_menu()
        elif secim == "4":
            print("Hava durumu modülü henüz eklenmedi.")
        elif secim == "5": 
            print("Cikis yapiliyor...")
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.")

if __name__ == "__main__":
    main_menu()
