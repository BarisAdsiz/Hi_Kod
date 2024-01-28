maas = float(input("Maaşınızı giriniz: "))

if(maas > 0):
    if(maas <= 10000):
        sonuc = maas * (5 / 100)
        maas-=sonuc
    elif(maas <= 25000):
        sonuc = maas * (10 / 100)
        maas-=sonuc
    elif(maas <= 45000):
        sonuc = maas * (25 / 100)
        maas-=sonuc
    else:
        sonuc = maas * (30 / 100)
        maas-=sonuc

    print(f"Maaşınızdan kesilen vergi {sonuc} TL'dir.")
    print(f"Yeni maaşınız {maas} TL'dir.")

else:
    print("hatalı maaş girdiniz! Lütfen 0 TL'den yüksek bir miktar giriniz")
