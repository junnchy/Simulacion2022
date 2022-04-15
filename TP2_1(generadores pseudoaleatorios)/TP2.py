
def metodosCuadrados():
    seed_number = int(input("Por favor ingrese un numero de cuatro digitos:\n[####] "))
    number = seed_number
    already_seen = set()
    counter = 0

    outFile = open("m2_output.txt", "w")


    while number not in already_seen:
        counter += 1
        already_seen.add(number)
        number = int(str(number * number).zfill(8)[2:6])  # zfill adds padding of zeroes
        print(f"#{counter}: {number}")

        writeValue = str(number)
        outFile.write(writeValue + "\n")
    
    outFile.close()

    print(f"Empezamos con{seed_number} y"
        f" el bloque se repite despues de {counter} pasos"
        f" con {number}.")


def GCLGenerator():
    pass

def generate_lcg( num_iterations ):
    """
    LCG - generates as many random numbers as requested by user, using a Linear Congruential Generator
    LCG uses the formula: X_(i+1) = (aX_i + c) mod m
    :param num_iterations: int - the number of random numbers requested
    :return: void
    """
    # Initialize variables
    x_value = 123456789.0    # Our seed, or X_0 = 123456789
    a = 101427               # Our "a" base value
    c = 321                  # Our "c" base value
    m = (2 ** 16)            # Our "m" base value


    # counter for how many iterations we've run
    counter = 0

    # Open a file for output
    outFile = open("lgc_output.txt", "w")

    #Perfom number of iterations requested by user
    while counter < num_iterations:
        # Store value of each iteration
        x_value = (a * x_value + c) % m
        

        #Obtain each number in U[0,1) by diving X_i by m
        writeValue = str(x_value/m)

        # write to output file
        outFile.write(writeValue + "\n")
        
        # print "num: " + " " + str(counter) +":: " + str(x_value)

        counter = counter+1

    outFile.close()
    print("Successfully stored " + str(num_iterations) + " random numbers in file named: 'lgc_output.txt'.")

def main():
    metodosCuadrados()
    generate_lcg(100)

main()
