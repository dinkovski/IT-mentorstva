from http.cookiejar import MONTHS_LOWER

cars = ["Audi", "Toyota", "Lexus"]
print(cars)
cars[1] = "Mercedes"
print(cars)
cars.append("Skoda")
print(cars)

# vezba - sortiranje cars po abecednom redu
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# trenutno na stanju imamo _____ automobila
print(f"trenutno na stanju imamo {len(cars)} automobila")

# dictionary
person = {
    "name": "Stf"
    "last_Name": "Milo"
    "age": 31
}
print(person["name"])
