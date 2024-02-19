import numpy as np

bir_boyutlu = np.array([1, 2, 3, 4, 5])

iki_boyutlu = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

uc_boyutlu = np.array([[[1, 2, 3],
                        [4, 5, 6]],
                       [[7, 8, 9],
                        [10, 11, 12]],
                       [[13, 14, 15],
                        [16, 17, 18]]])

print("Bir Boyutlu Dizi:")
print("İlk eleman:", bir_boyutlu[0])
print("İlk üç eleman:", bir_boyutlu[:3])
print()

print("İki Boyutlu Dizi:")
print("İlk satır:", iki_boyutlu[0])
print("İlk eleman:", iki_boyutlu[0, 0])
print("İlk sütun:", iki_boyutlu[:, 0])
print("İlk iki satır:", iki_boyutlu[:2])
print()

print("Üç Boyutlu Dizi:")
print("İlk matris:", uc_boyutlu[0])
print("İlk matrisin ilk satırı:", uc_boyutlu[0, 0])
print("İlk matrisin ilk elemanı:", uc_boyutlu[0, 0, 0])
print("İlk matrisin ilk sütunu:", uc_boyutlu[:, 0])
print("İlk matrisin ilk iki satırı:", uc_boyutlu[0, :2])
