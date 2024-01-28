kullanici = str(input("Kullanıcı adı giriniz: "))
sifre = str(input("Şifre giriniz: "))


if(len(sifre) >= 6):
    print("Hesap oluşturuldu")
else: 
    print("Şifre 6 haneden az olamaz lütfen tekrar deneyin")