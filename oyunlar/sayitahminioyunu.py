import random

def sayi_tahmin():
    hedef = random.randint(1, 100)
    tahmin = None
    deneme = 0

    print("1 ile 100 arasında bir sayı tuttum. Tahmin et!")

    while tahmin != hedef:
        try:
            tahmin = int(input("Tahminin: "))
            deneme += 1
            if tahmin < hedef:
                print("Daha büyük bir sayı dene!")
            elif tahmin > hedef:
                print("Daha küçük bir sayı dene!")
            else:
                print(f"Tebrikler! {deneme} denemede buldun.")
        except ValueError:
            print("Lütfen bir sayı gir.")
