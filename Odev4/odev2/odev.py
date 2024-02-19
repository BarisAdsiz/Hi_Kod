liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
yeni_liste = []

for eleman in liste:
    if isinstance(eleman, str):
        yeni_liste.append(eleman)

print(yeni_liste)
