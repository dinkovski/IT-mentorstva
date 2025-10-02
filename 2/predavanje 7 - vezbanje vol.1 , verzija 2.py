products = {
    "hleb": {
        "cena": 100,
        "kolicina": 50
    },
    "pivo": {
        "cena": 150,
        "kolicina": 220
    },
    "makarone": {
        "cena": 330,
        "kolicina": 90
    }
}

print(products)

# pitati korisnika da unese ime proizvoda koji zeli da obrise
# koji proizvod zelite da obrisete?

product = None
action = None
while action not in ["Brisanje proizvoda","Dodavanje proizvoda, Izlistavanje proizvoda"]:
    action = input("Sta zelite da uradite? (Brisanje proizvoda, Dodavanje proizvoda, Izlistavanje proizvoda) ")
    if action == "Brisanje proizvoda":
        while product not in products:
          product = input("Unesite ime proizvoda za brisanje: ").lower()
        del products[product]
        action = None

    elif action == "Dodavanje proizvoda":
            product = input("Unesite ime proizvoda koji ne postoji ").lower()
            products[product] = {}
            new_product_price = input("Unesite cenu novog proizvoda: ").lower()
            products[product]["cena"] = new_product_price
            new_product_amount = input("Unesite kolicinu novog proizvoda: ")
            products[product]["kolicina"] = new_product_amount
            print("DODAT PROIZVOD")

    elif action == "Izlistavanje proizvoda":
        print(products)

print(products)

#dodati proizvod - cap sensitive i ne sme biti manje od 2 karaktera


