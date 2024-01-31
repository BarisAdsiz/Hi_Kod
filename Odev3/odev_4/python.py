from datetime import date

dogumYili = int(input("Doğum yılınızı girin: "))
isim = input("Adınızı girin: ")

def EmekliHesapla(dogumYili, isim):
    def YasHesapla(dogumYili):
        today = date.today()
        yas = today.year - dogumYili
        return yas

    yas = YasHesapla(dogumYili)

    if yas >= 65:
        print(f"{isim}, emekli oldunuz.")
    else:
        emekliYas = 65
        kalanYil = emekliYas - yas
        print(f"{isim}, emekliliğinize {kalanYil} yıl kaldı.")

EmekliHesapla(dogumYili, isim)