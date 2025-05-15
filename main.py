from hesapmakinesi import hesapmakinesi_menu
from oyunlar import oyunlar_menu
from dovizkuru import dovizkuru_menu
from havadurumu import havadurumu_menu
from haberler import haberler_menu
from kripto import kripto_menu
from bilgikutusu import bilgikutusu_menu

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
        print("║  5- Haberler        ║")
        print("║  6- Kripto          ║")
        print("║  7- Soru Sor        ║")
        print("║  8- Cıkıs           ║")
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
            havadurumu_menu.havadurumu_menu()
        elif secim=="5":
            haberler_menu.haberler_menu()
        elif secim == "6": 
            kripto_menu.kripto_menu()
        elif secim == "7": 
            bilgikutusu_menu.bilgikutusu_menu()     
        elif secim == "8": 
            print("Cikis yapiliyor...")
            break
        
        else:
            print("Geçersiz seçim! Tekrar deneyin.")

if __name__ == "__main__":
    main_menu()
