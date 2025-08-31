#vezba - ako korisnik ima vise od 18 godina ispisati "punoletni ste
#ako ima manje od 18, ispisati "niste punoletni"

age = 13
allowed_age = 18


if age >= allowed_age:
    print("punoletni ste")
else:
    print("niste punoletni")

age_difference = age - allowed_age
print(f"broj godina preko neophodnog - {age_difference}")