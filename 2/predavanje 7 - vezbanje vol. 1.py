from os import remove

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
# pitati korisnika da unese ime proizvoda koji zeli da obrise
# koji proizvod zelite da obrisete?


action = input("Sta zelite da uradite? (Brisanje proizvoda, Dodavanje proizvoda) ")
if action == ("Brisanje proizvoda"):
    while product not in products:
            product = input("Unesite ime proizvoda za brisanje: ").lower()
    del products[product]

elif action == "dodavanje proizvoda":
    new_product_name = input("Unesite ime novog proizvoda: ").lower()
    products[new_product_name] = {}
    new_product_price = input("Unesite cenu novog proizvoda: ").lower()
    products[new_product_name]["cena"] = new_product_price
    new_product_amount = input("Unesite kolicinu novog proizvoda: ")
    products[new_product_name]["kolicina"] = new_product_amount



print(products)



# pitati korisnika sta zeli da uradi - obrise ili doda proizvode ("test")
