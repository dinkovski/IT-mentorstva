# vezba 1
# lista 3 proizvoda: iPhone 14, 15, Samsung S23
# napisati proveru koja gleda da li postoji "iPhone 14" u listi

products = ["iPhone 14", "iPhone 15", "Samsung S23"]
products = products.lower

#napraviti posebnu varijablu za ono sto trazim
search_item = input("Unesite ime telefona koji trazite")
print("KORISNIK JE UNEO " + search_item)

if search_item in products:
    print("pronasli smo sta ste hteli")
else:
    print("nismo pronasli trazeni proizvod")

