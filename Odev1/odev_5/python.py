hiKod = "Hi-Kod Veri Bilimi Atölyesi"

veri = hiKod[7:11]
bilimi = hiKod[12:18]
atolyesi = hiKod[19:]

buyukHarf = hiKod.upper()

kucukHarf = hiKod.lower()

print(f"Her bir kelime: \nHi-kod: {hiKod[:6]} \nVeri: {hiKod[7:11]} \nBilimi:{hiKod[12:18]} \nAtölyesi: {hiKod[19:]}")

print(f"\nHepsini büyük harfe çevirme: {buyukHarf}")
print(f"\nHepsini küçük harfe çevirme: {kucukHarf}")