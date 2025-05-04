import requests

def dovizkuru_menu():
    print("\n--- Döviz Kuru ---")

    try:
        print("API isteği gönderiliyor...")
        response = requests.get("https://open.er-api.com/v6/latest/TRY")
        data = response.json()

       # print("Gelen veri:", data)  # Geçici kontrol satırı

        rates = data.get("rates")
        if rates is None:
            raise ValueError("API 'rates' verisini döndürmedi!")

        usd = rates["USD"]
        eur = rates["EUR"]
        gbp = rates["GBP"]

        print(f"\n1 Türk Lirası şu anda:")
        print(f"  {usd:.2f} USD")
        print(f"  {eur:.2f} EUR")
        print(f"  {gbp:.2f} GBP")

    except Exception as e:
        print("Veriler alınamadı! Hata:", e)

    input("\nAna menüye dönmek için Enter'a bas...")

if __name__ == "__main__":
    dovizkuru_menu()
