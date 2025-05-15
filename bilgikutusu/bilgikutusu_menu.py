import requests
import urllib.parse

# 🔧 İstediğin kadar artır: 1000 → daha uzun açıklama
KARAKTER_LIMITI = 1000

def bilgikutusu_menu():
    print("\n--- Bilgi Kutusu (Soru-Cevap) ---")

    try:
        soru = input("Kısa bir soru yazın (örnek: Atatürk kimdir?): ").strip()
        if not soru:
            print("Boş soru girilemez.")
            return

        cevap = None
        gorsel = None

        # 🔎 Soru analizi ve temiz başlık çıkarımı
        orijinal_soru = soru.lower()
        if " nerede" in orijinal_soru:
            temiz_soru = orijinal_soru.replace(" nerede", "").strip()
        elif " nedir" in orijinal_soru:
            temiz_soru = orijinal_soru.replace(" nedir", "").strip()
        elif " kimdir" in orijinal_soru:
            temiz_soru = orijinal_soru.replace(" kimdir", "").strip()
        elif " ne zaman" in orijinal_soru:
            temiz_soru = orijinal_soru.replace(" ne zaman", "").strip()
        else:
            temiz_soru = (
                orijinal_soru.replace("ne demek", "")
                .replace("nelerdir", "")
                .replace("kaç", "")
                .replace("?", "")
                .strip()
            )

        # 📌 Sabit veriler (Ekonomi, Savunma, Eğitim)
        sabit_cevaplar = {
            "2025 enflasyon": """Türkiye’de 2025 için yıl sonu enflasyon tahmini %36’dır. 
2024 sonunda TÜİK’e göre enflasyon %64,8 olarak gerçekleşmiştir.""",

            "merkez bankası faiz": "2025 itibarıyla TCMB politika faizi %50'dir (Mayıs 2025).",

            "gsymh büyüme oranı": "2024 yılında Türkiye ekonomisi %4,5 oranında büyümüştür (TÜİK).",

            "savunma sanayi şirketleri": """Türkiye'nin en büyük savunma sanayi firmaları:
1. ASELSAN
2. TUSAŞ (TAI)
3. ROKETSAN
4. HAVELSAN
5. STM
6. BMC
7. FNSS
8. Otokar""",

            "milli muharip uçak": "KAAN, 2025’te ilk uçuşunu yaptı. 2028’de TSK envanterine girmesi hedefleniyor.",

            "üniversite sayısı": "2025 itibarıyla Türkiye'de 208 üniversite var: 131 devlet, 75 vakıf, 2 vakıf MYO.",

            "öğrenci sayısı": "2024-2025 döneminde yükseköğretimde 8,4 milyon öğrenci bulunuyor.",

            "okullaşma oranı": "6-13 yaş grubunda okullaşma oranı %98,2'dir (MEB 2024)."
        }

        for anahtar, sabit in sabit_cevaplar.items():
            if anahtar in temiz_soru:
                cevap = sabit
                break

        # 🔍 DuckDuckGo API
        if not cevap:
            ddg_url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(soru)}&format=json&no_redirect=1"
            ddg = requests.get(ddg_url).json()

            if ddg.get("AbstractText"):
                cevap = ddg["AbstractText"]
            elif ddg.get("Heading"):
                cevap = ddg["Heading"]
            else:
                rel = ddg.get("RelatedTopics")
                if isinstance(rel, list) and rel:
                    cevap = rel[0].get("Text")

        # 🔁 Vikipedi extract + REST summary + görsel
        if not cevap:
            print("🔁 DuckDuckGo sonuç vermedi, Vikipedi'den aranıyor...")

            baslik_haritasi = {
                "türkiye": "Türkiye Cumhuriyeti",
                "atatürk": "Mustafa Kemal Atatürk",
                "sabancı": "Sabancı ailesi",
                "osmanlı": "Osmanlı İmparatorluğu",
                "openai": "OpenAI",
                "cumhuriyet": "Türkiye Cumhuriyeti",
                "python": "Python (programlama dili)",
                "fenerbahçe": "Fenerbahçe (spor kulübü)"
            }

            kullanilacak_baslik = baslik_haritasi.get(temiz_soru, temiz_soru.title())
            encoded_title = urllib.parse.quote(kullanilacak_baslik.replace(" ", "_"))

            # Extracts API
            wiki_params = {
                "action": "query",
                "prop": "extracts",
                "explaintext": True,
                "format": "json",
                "titles": kullanilacak_baslik
            }

            wiki = requests.get("https://tr.wikipedia.org/w/api.php", params=wiki_params).json()
            pages = wiki.get("query", {}).get("pages", {})
            for p in pages.values():
                metin = p.get("extract", "").strip()
                if metin:
                    cevap = metin[:KARAKTER_LIMITI] + ("..." if len(metin) > KARAKTER_LIMITI else "")
                    break

            # REST API (fallback + görsel)
            if not cevap:
                print("🔁 Vikipedi ‘extracts’ boş, REST summary API deneniyor...")
                rest_url = f"https://tr.wikipedia.org/api/rest_v1/page/summary/{encoded_title}"
                rest = requests.get(rest_url).json()
                extract = rest.get("extract", "").strip()
                if extract:
                    cevap = extract[:KARAKTER_LIMITI] + ("..." if len(extract) > KARAKTER_LIMITI else "")
                gorsel = rest.get("thumbnail", {}).get("source")

        # ✅ Yazdır
        if cevap:
            print(f"\n📌 Cevap:\n{cevap}")
            if gorsel:
                print(f"\n🖼️ Görsel: {gorsel}")
        else:
            print("❗ Bu konuda özet bilgi bulunamadı.")
            print(f"🔗 Vikipedi’de incelemek istersen: https://tr.wikipedia.org/wiki/{encoded_title.replace('%20', '_')}")

    except Exception as e:
        print("⚠️ Bilgi alınamadı! Hata:", e)

    input("\nAna menüye dönmek için Enter'a bas...")
