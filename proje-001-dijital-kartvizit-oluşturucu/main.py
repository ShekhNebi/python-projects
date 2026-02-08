isim = input("Lütfen isminizi giriniz: ").strip().title()
soyisim = input("Lütfen soyisminizi giriniz: ").strip().upper()
unvan = input("Lütfen ünvanınızı giriniz: ").strip().title()
iletisim = input("Lütfen iletişim bilgilerinizi giriniz: ").strip()

genislik = 30

print()
print("*" * genislik)
print(f"{'DİJİTAL KARTVİZİT':^{genislik}}") 
print("*" * genislik)

print(f"Ad Soyad : {isim} {soyisim}") 
print(f"Ünvan    : {unvan}") 
print(f"İletişim : {iletisim}")

print("*" * genislik)