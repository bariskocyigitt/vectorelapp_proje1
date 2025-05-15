import requests

def havadurumu_menu():
    print("\n--- Hava Durumu ---")
    sehir = input("Hangi şehrin hava durumunu öğrenmek istersiniz?: ").strip()

    try:
        print("\nHava verileri alınıyor...")

        # JSON formatında 3 günlük detaylı veri al
        url = f"https://wttr.in/{sehir}?format=j1"
        
        response = requests.get(url)
        
        data = response.json()


        # Güncel sıcaklık
        anlik = data["current_condition"][0]
        print(f"\n📍 {sehir.title()} - Anlık Durum:")
        print(f"  Sıcaklık      : {anlik['temp_C']}°C")
        print(f"  Hissedilen    : {anlik['FeelsLikeC']}°C")
        print(f"  Rüzgar        : {anlik['windspeedKmph']} km/h")
        print(f"  Açıklama      : {anlik['weatherDesc'][0]['value']}")

        # 3 günlük tahmin
        print(f"\n📅 {sehir.title()} için 3 Günlük Tahmin:")
        for i in range(3):
            gun = data["weather"][i]
            tarih = gun["date"]
            maxtemp = gun["maxtempC"]
            mintemp = gun["mintempC"]
            aciklama = gun["hourly"][4]["weatherDesc"][0]["value"]  # öğlen saatine göre
            print(f"  {tarih} → {aciklama} | {mintemp}°C - {maxtemp}°C")

    except Exception as e:
        print("Veriler alınamadı! Hata:", e)

    input("\nAna menüye dönmek için Enter'a bas...")
