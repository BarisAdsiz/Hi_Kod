hak = 3
while True:
    password = "muserref"
    sifre = str(input("Lütfen şifre giriniz: "))

    if sifre == password:
        print("Giriş yapıldı")
        break
    else:
        print("Şifre yanlış girildi!")
        hak -= 1
        print(f"Kalan hakkınız {hak}")
        if hak <= 0:
            print("Hakkınız kalmadı!")
            break