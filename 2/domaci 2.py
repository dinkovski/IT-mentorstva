# napraviti dictionary koji ima sledecu strukturu
# person1: "name": "Toma", "last_name": "Nikolic",
from main import last_name

People = {
    "Person1": {
        "name": "Toma",
        "last_name": "Nikolic"
    },
    "Person2": {
        "name": "Petar",
        "last_name": "Folic"
    },
    "Person3": {
        "name": "Dragan",
        "last_name": "Draganic"
    }
}
print(People["Person3"]["last_name"], People["Person3"]["name"])
print(People["Person3"]["name"], People["Person1"]["name"])
