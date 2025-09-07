# napisati petlju koja ispisuje brojeve od 0 do 100

for number in range(20):
    if number == 10:
        continue
    if number == 16:
        break
    if number%2 == 0:
        print(f"broj je paran {number}")