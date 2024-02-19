import numpy as np

matris = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

dortluk_dizi = np.array([[[1, 2, 3],
                          [4, 5, 6]],
                         [[7, 8, 9],
                          [10, 11, 12]]])

print("Matris:")
print("Boyut:", matris.ndim)
print("Eleman Sayısı:", matris.size)
print("Satır-Sütun:", matris.shape)
print()

print("Dörtlük Dizi:")
print("Boyut:", dortluk_dizi.ndim)
print("Eleman Sayısı:", dortluk_dizi.size)
print("Satır-Sütun-derinlik:", dortluk_dizi.shape)
print()

print("Matrisin 2. satırı:", matris[1])
print("Matrisin (1, 2) elemanı:", matris[1, 2])
print()

print("Dörtlük dizinin (1, 0, 2) elemanı:", dortluk_dizi[1, 0, 2])
print()

print("Matrisin ilk iki satırı:")
print(matris[:2])
print()

print("Dörtlük dizinin ilk matrisi:")
print(dortluk_dizi[0])
