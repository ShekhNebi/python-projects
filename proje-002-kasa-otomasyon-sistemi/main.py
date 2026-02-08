fiyat_domates = 35.00
fiyat_biber = 40.00
fiyat_patlican = 30.00

kg_domates = float(input("Kaç kilo domates istiyorsunuz: "))
kg_biber = float(input("Kaç kilo biber istiyorsunuz: "))
kg_patlican = float(input("Kaç kilo patlıcan istiyorsunuz: "))

toplam = (fiyat_domates*kg_domates) + (fiyat_biber*kg_biber) + (fiyat_patlican*kg_patlican)

genislik = 30

print()
print(f"{'Alışveriş Özeti' : ^{genislik}}")
print(genislik * "-")
print(f"{kg_domates} kg domates, {kg_biber} kg biber, {kg_patlican} kg patlıcan")
print(f"Toplam {toplam:.2f} Tl")