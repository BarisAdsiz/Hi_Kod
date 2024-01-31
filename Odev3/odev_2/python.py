sayi = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))
def faktoriyel_dongu(n):
    fkt = 1
    for i in range(1, n + 1):
        fkt *= i
    return fkt

print(f"{sayi}! = {faktoriyel_dongu(sayi)}")
