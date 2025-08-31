name = "admine"
password = "mojaSifra"

if name == "admin" and password == "mojaSifra":
    print("dobrodosao admire")
else:
    print("ne moze jbg, niste admir")

#ako je ime toma i ako je sifra 12345 - print dobrodosao tomo
#ako je ime admin i ako je sifra 224466 - print welcome, admin
#else print "pogresna sifra ili ime"

name = "Toma"
password = "12345"

if name.lower() == "Toma" and password == "12345":
    print("dobrodosao, Tomo")
elif name.lower() == "admin" and password == "224466":
    print("welcome, admine!")
else:
    print("niste administrator, pogresna sifra ili ime")