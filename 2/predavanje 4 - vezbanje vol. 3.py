# napisati program da korisnik ubaci ime proizvoda, a zatim dobije cenu tog proizvoda
# ako proizvod ne postoji, ispisati poruku "Proizvod nije pronadjen"

products = {"Macbook Air M4": 969, "iPhone 15": 1200, "Samsung S23": 1200}
lower_products = [item.lower() for item in products]

search_item = input("Napisite ime proizvoda: ").lower()
print("Pretraga za artikal " + search_item)

if search_item in lower_products:
    print(lower_products[search_item])
else:
    print("Proizvod nije pronadjen")

