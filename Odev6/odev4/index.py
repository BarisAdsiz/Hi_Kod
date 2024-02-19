import numpy as np

sifir_matris = np.zeros((3, 3))

bir_matris = np.ones((3, 3))

birlesik_matris_satir = np.concatenate((sifir_matris, bir_matris), axis=0)

birlesik_matris_sutun = np.concatenate((sifir_matris, bir_matris), axis=1)

print("Satır bazında birleştirilmiş matris:")
print(birlesik_matris_satir)
print()

print("Sütun bazında birleştirilmiş matris:")
print(birlesik_matris_sutun)
