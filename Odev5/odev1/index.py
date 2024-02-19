ogrenciNot = {
    "Baris": {"Matematik": 90, "Fizik": 85, "Kimya": 70},
    "Muserref": {"Matematik": 75, "Fizik": 80, "Kimya": 95},
    "Ezgi": {"Matematik": 85, "Fizik": 75, "Kimya": 80}
}

ogrenciAdi = input("Öğrencinin adını girin: ")
dersAdi = input("Notunu öğrenmek istediğiniz dersin adını girin (Matematik, Fizik, Kimya): ")

if ogrenciAdi in ogrenciNot:
    if dersAdi in ogrenciNot[ogrenciAdi]:
        notu = ogrenciNot[ogrenciAdi][dersAdi]
        print(f"{ogrenciAdi}'nin {dersAdi} dersindeki notu: {notu}")
    else:
        print(f"{ogrenciAdi} isimli öğrencinin {dersAdi} dersine ait not bilgisi bulunmamaktadır.")
else:
    print(f"{ogrenciAdi} isimli öğrenci bulunamadı.")
