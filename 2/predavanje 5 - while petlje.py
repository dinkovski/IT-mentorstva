# pitaj korisnika koliko ima godina
# ako nije uneo pitaj opet

age = ""

while not age.isdigit() or int(age) < 18:
    age = input("Koliko imas godina? ")
print(age)