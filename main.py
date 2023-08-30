name = input("Imię zwierzaka: ")
weight = float(input("Waga: "))
sex = input("Płeć: ")
fiv_felv = input("Czy stwierdzono FIV/FeLv? (Tak/Nie): ").upper()
castration_sterilization = input("Czy kot jest wykastrowany/wysterylizowany?(Tak/Nie): ").upper()

data = {"name": name, "weight": weight, "sex": sex, "fiv_felv": fiv_felv, "castration": castration_sterilization}

print(data)