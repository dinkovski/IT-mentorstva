#korisnik treba da unese cenu korpe
# ako je cena preko ili 1000 dinara, ispisati koliki popust su ostvarili
#ako je cena ispod 1000, ispisati "Vasa korpa iznosi xy"

price = int(input("Unesite cenu korpe: "))

if price >= 1000:
    tax_amount = price * 0.1
    print(f"Ostvarili ste 10% popusta, ukupan iznos {tax_amount} evra")
else:
    print("Vasa Korpa iznosi " + str(price))
