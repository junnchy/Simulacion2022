
def metodosCuadrados():
    seed_number = int(input("Por favor ingrese un numero de cuatro digitos:\n[####] "))
    number = seed_number
    already_seen = set()
    counter = 0

    while number not in already_seen:
        counter += 1
        already_seen.add(number)
        number = int(str(number * number).zfill(8)[2:6])  # zfill adds padding of zeroes
        print(f"#{counter}: {number}")

    print(f"Empezamos con{seed_number} y"
        f" el bloque se repite despues de {counter} pasos"
        f" con{number}.")


def main():
    metodosCuadrados()

main()
