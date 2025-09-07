#nestovani dictionary
# svaka prodavnica ima svoje ime, ima svoje proizvode i njihove cene

shops = {
    "Maxi": {
        "Hleb": 100,
        "novine": 50,
    },
    "Idea": {
        "Hleb": 90,
        "novine": 40,
    },
    "Linda": {
        "Hleb": 80,
        "novine": 60,
    },
    "Aroma": {
        "Hleb": 200,
        "novine": 40,
    },
}
# ispisati petlju koja ce ispisati sve cene hleba

ukupna_cena_leba = 0
broj_prodavnica_sleba = 0
max_cena = 0
ime_max_shopa = ""

for ime_prodavnice, artikli in shops.items():
    if "Hleb" in artikli:
        ukupna_cena_leba += artikli["Hleb"]
        broj_prodavnica_sleba += 1
        if max_cena < artikli["Hleb"]:
            max_cena = artikli["Hleb"]
            ime_max_shopa = ime_prodavnice
print(ukupna_cena_leba)

ukupan_broj_prodavnica = len(shops)

print(ukupan_broj_prodavnica)

prosecna_cena_leba = ukupna_cena_leba / broj_prodavnica_sleba
print(prosecna_cena_leba)
print(max_cena, ime_max_shopa)



