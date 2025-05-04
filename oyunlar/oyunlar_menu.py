from oyunlar import adamasmaca
from oyunlar import tetris
from oyunlar import sayitahminioyunu
from oyunlar import taskagitmakas
from oyunlar import mayintarlasi

def oyunlar_menu():
    while True:
        print("\n\033[1;32;40m")
        print("╔═══════════════════════════╗")
        print("║          Oyunlar          ║")
        print("║  1-Adam Asmaca            ║")
        print("║  2-Tetris                 ║")
        print("║  3-Sayi Tahmin Oyunu      ║")
        print("║  4-Tas-Kagit-Makas Oyunu  ║")
        print("║  5-Mayin Tarlasi          ║")
        print("║  6-Ana Menüye Dön         ║")
        print("╚═══════════════════════════╝")

        secim = input("Seçiminiz: ")

        if secim == "1":
            adamasmaca.adam_asmaca()
        elif secim == "2":
            tetris.tetris()
        elif secim == "3":
            sayitahminioyunu.sayi_tahmin()
        elif secim == "4":
            taskagitmakas.tas_kagit_makas()
        elif secim == "5":
            mayintarlasi.mayin_tarlasi()
        elif secim == "6":
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.")
