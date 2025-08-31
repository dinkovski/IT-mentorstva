#ako je tajni 4231 ili ako je tajni pin 3124 ispisati poruku "PIN JE TACAN"
# u suprotnom izbaciti poruku "NETACAN PIN!"
# zabranjeno koriscenje vise od 1 IF-a i zabranjeno koriscenje elif
# dozvoljeno 1 if + 1 else

tajni_pin = "3124"

if tajni_pin == "4231" or tajni_pin == "3124":
    print("PIN JE TACAN")
else:
    print("NETACAN PIN!")
