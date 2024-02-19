ogrenciAdi = {
    "Baris": {"Matematik": 90, "Fizik": 85, "Kimya": 70},
    "Muserref": {"Matematik": 75, "Fizik": 80, "Kimya": 95},
    "Ezgi": {"Matematik": 85, "Fizik": 75, "Kimya": 80}
}

while True:
    print("\n1. Öğrenci notlarını görüntüle")
    print("2. Yeni öğrenci notu ekle")
    print("3. Öğrenci notlarını güncelle")
    print("4. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == "1":
        ogrenci_adi = input("Öğrencinin adını girin: ")
        if ogrenci_adi in ogrenciAdi:
            print(f"{ogrenci_adi}'nin notları:")
            for ders, notu in ogrenciAdi[ogrenci_adi].items():
                print(f"{ders}: {notu}")
        else:
            print(f"{ogrenci_adi} isimli öğrenci bulunamadı.")

    elif secim == "2":
        ogrenci_adi = input("Yeni öğrencinin adını girin: ")
        if ogrenci_adi in ogrenciAdi:
            print("Bu isimde bir öğrenci zaten var.")
        else:
            matNot = int(input("Matematik notunu girin: "))
            fizikNot = int(input("Fizik notunu girin: "))
            kimyaNot = int(input("Kimya notunu girin: "))
            ogrenciAdi[ogrenci_adi] = {"Matematik": matNot, "Fizik": fizikNot, "Kimya": kimyaNot}
            print(f"{ogrenci_adi} isimli yeni öğrenci eklendi.")

    elif secim == "3":
        ogrenci_adi = input("Notunu güncellemek istediğiniz öğrencinin adını girin: ")
        if ogrenci_adi in ogrenciAdi:
            dersAdi = input("Güncellemek istediğiniz dersin adını girin (Matematik, Fizik, Kimya): ")
            if dersAdi in ogrenciAdi[ogrenci_adi]:
                yeniNot = int(input(f"Yeni {dersAdi} notunu girin: "))
                ogrenciAdi[ogrenci_adi][dersAdi] = yeniNot
                print(f"{ogrenci_adi}'nin {dersAdi} dersine ait not güncellendi.")
            else:
                print(f"{ogrenci_adi} isimli öğrencinin {dersAdi} dersine ait bir not bilgisi bulunmamaktadır.")
        else:
            print(f"{ogrenci_adi} isimli öğrenci bulunamadı.")

    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
