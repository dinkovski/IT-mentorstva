# pitati korisnika da unese ime proizvoda
# kada unese ime proizvoda dodati proizvod u kasu
# korisnik mora uneti 3 proizvoda ukupno

kasa = list()

while len(kasa) < 3:
    proizvod = input("Unesite ime proizvoda ")
    kasa.append(proizvod)
    print(kasa)