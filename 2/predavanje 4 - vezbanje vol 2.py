#pitati korisinika za godine
# ako ima preko 18 ispisati "punoletni ste"
# ako ima manje "maloletni ste"

age = int(input("unesite broj godina"))
# ako korisnik ispise bilo sta manje od 0, ispisati gresku i zaustaviti program

if age < 0:
    print("godine ne mogu biti manje od 0")
    quit()

if age <= 12:
    print("Vi ste dete")
elif age >= 13 and age < 18:
    print("Vi ste tinejdzer")
elif age >= 18 and age < 65:
    print("Vi ste odrasla osoba")
elif age > 64:
    print("Vi ste penzioner")
