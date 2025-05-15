def kripto_menu():
    print("\n--- Kripto Para Kurları (Geçici Offline - USD) ---")

    # Gerçekçi sabit fiyatlar (elle güncellenebilir)
    btc_usd = 100000  # 1 BTC = 100.000 $
    eth_usd = 5000    # 1 ETH = 5.000 $

    print(f"\n🪙 Bitcoin (BTC): ${btc_usd:,}")
    print(f"🪙 Ethereum (ETH): ${eth_usd:,}")

    try:
        # BTC alımı hesaplama
        miktar_btc = float(input("\nKaç $'lık BTC almak istiyorsunuz?: "))
        btc_alinabilir = miktar_btc / btc_usd
        print(f"${miktar_btc:,.2f} ≈ {btc_alinabilir:.8f} BTC")

        # ETH alımı hesaplama
        miktar_eth = float(input("\nKaç $'lık ETH almak istiyorsunuz?: "))
        eth_alinabilir = miktar_eth / eth_usd
        print(f"${miktar_eth:,.2f} ≈ {eth_alinabilir:.8f} ETH")

    except:
        print("Geçerli bir sayı girilmedi.")

    input("\nAna menüye dönmek için Enter'a bas...")
