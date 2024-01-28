while True:
    kullanici = str(input("Kullanıcı adı giriniz: "))
    sifre = str(input("Şifre giriniz: "))
    
    if 5 <= len(sifre) <= 10:
        print("Hesap oluşturuldu")
        break
    else: 
        print("Şifre 6 haneden az olamaz lütfen tekrar deneyin")