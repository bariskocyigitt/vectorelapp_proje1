import requests

def haberler_menu():
    print("\n--- Güncel Haberler ---")
    kategori = input("Haber kategorisi (genel, spor, teknoloji, sağlık): ").lower()

    API_KEY = "549893d19cd81b06d1c7b47056d0cc36"  # ← Buraya kendi anahtarını gir
    url = f"https://gnews.io/api/v4/top-headlines?lang=tr&country=tr&topic={kategori}&max=5&apikey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        haberler = data.get("articles", [])
        if not haberler:
            print("Hiç haber bulunamadı veya kategori geçersiz.")
            return

        print(f"\n📢 {kategori.title()} kategorisinden en güncel 5 haber:\n")
        for i, haber in enumerate(haberler, 1):
            print(f"{i}. {haber['title']}")
            print(f"   {haber['url']}\n")

    except Exception as e:
        print("Haberler alınamadı! Hata:", e)

    input("\nAna menüye dönmek için Enter'a bas...")
