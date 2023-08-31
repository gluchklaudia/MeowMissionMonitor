import json


def load_data_from_file():
    with open("data_file.json", "r") as file:
        data = json.load(file)
    return data

data = load_data_from_file()

name = input("Imię zwierzaka: ")
weight = float(input("Waga: "))
sex = input("Płeć: ")
fiv_felv = input("Czy stwierdzono FIV/FeLv? (Tak/Nie): ").upper()
castration_sterilization = input("Czy kot jest wykastrowany/wysterylizowany?(Tak/Nie): ").upper()

data.append({"name": name, "weight": weight, "sex": sex, "fiv_felv": fiv_felv, "castration": castration_sterilization})

with open("data_file.json", "w") as file:
    json.dump(data, file)




