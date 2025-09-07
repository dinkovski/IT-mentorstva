# array 5 studenata
# svaki student name: , score 0-100, active: true/false

students = [
    {
        "name": "Toma",
        "score": 45,
        "active": True
    },
    {
        "name": "Rade",
        "score": 92,
        "active": False
    },
    {
        "name": "Sale",
        "score": 15,
        "active": True
    },
    {
        "name": "Smrade",
        "score": 32,
        "active": True
    }
]

# napisati petlju koja ispisuje samo aktivne studente
# ispisati ocene za aktivne studente



for student in students:
    if student["active"] == False:
        continue

    if student ["score"] >= 80:
        student["grade"] = "A"
    elif student["score"] >= 60 and student["score"] < 80:
        student["grade"] = "B"
    elif student["score"] >= 40 and student["score"] < 60:
        student["grade"] = "C"
    elif student["score"] >= 20 and student["score"] < 60:
        student["grade"] = "D"
    else:
        student["grade"] = "F"

print(students)