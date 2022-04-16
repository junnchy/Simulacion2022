#BLOQUE DE GENERADORES

def metodosCuadrados(num_iterations):
    seed_number = int(input("Por favor ingrese un numero de cuatro digitos:\n[####] "))
    number = seed_number
    already_seen = set()
    counter = 0

    outFile = open("m2_output.txt", "w")


    #while number not in already_seen:
    for i in range(num_iterations):
        #counter += 1
        #already_seen.add(number)
        number = int(str(number * number).zfill(8)[2:6])  # zfill adds padding of zeroes
        #print(f"#{counter}: {number}")
        aux = number/10000
        writeValue = str(aux)
        outFile.write(writeValue + "\n")
    
    outFile.close()

    """  
        print(f"Empezamos con{seed_number} y"
        f" el bloque se repite despues de {counter} pasos"
        f" con {number}.")
    """


def generate_gcl_rand( num_iterations ):
    """
    GCL rand - genera tantos numeros como los solicitados por el usuario, usando un Generador Lineal Congruencial
    GLC rand usa la fotmula: X_(i+1) =  (7^5)*X_i*mod(2^31 - 1) == (aX_i + c) mod m
    :param num_iterations: int - el numero de numeros aleatorios solicitados
    :return: void
    """
    # Inicializacion de Variables
    x_value = 123456789.0    # Our seed, or X_0 = 123456789
    a = (7**5)               # Our "a" base value
    c = 0                  # Our "c" base value
    m = (2 ** 31) - 1            # Our "m" base value
    
    counter = 0 # Variable counter es el contador de iteraciones
    outFile = open("lgc_rand_output.txt", "w") # Apertura del documento que almancenara los resultados del generador

    #Ejecuta la funcion del generador con el limite establecido previamente
    while counter < num_iterations:
        x_value = (a * x_value + c) % m
        writeValue = str(x_value/m) #Obtain each number in U[0,1) by diving X_i by m
        outFile.write(writeValue + "\n")
        counter += 1

    outFile.close()
    print("Successfully stored " + str(num_iterations) + " random numbers in file named: 'lgc_output.txt'.")


def generate_gcl_randu(num_iterations):
    """
    LCG RANDU- generates as many random numbers as requested by user, using a Linear Congruential Generator
    LCG uses the formula: X_(i+1) = (aX_i + c) mod m.

    This LCG uses the RANDU initial setting, a=65539; c=0; m=2^31.
    RANDU is known to have an issue: its values fall into 15 parallel 2D planes.
    So while its pseudo-randomness is enough for some applications. It's not great.
    Not crypto strength by any means.

    :param num_iterations: int - the number of random numbers requested
    :return: void
    """
    # Initialize variables
    x_value = 123456789.0    # Our seed, or X_0 = 123456789
    a = 65539                # Our "a" base value
    c = 0                    # Our "c" base value
    m = (2 ** 31)            # Our "m" base value

    
    counter = 0 # counter for how many iterations we've run

    outFile = open("lgc_RANDU_output.txt", "w")  # Open a file for output

    #Perfom number of iterations requested by user
    while counter < num_iterations:
        x_value = (a * x_value + c) % m
        writeValue = str(x_value/m) #Obtain each number in U[0,1) by diving X_i by m
        outFile.write((writeValue + "\n"))
        counter +=1

    outFile.close()
    print ("Successfully stored " + str(num_iterations) + " random numbers in file named: 'lgc_RANDU_output.txt'.")

def main():
    metodosCuadrados(100)
    generate_gcl_rand(100)
    generate_gcl_randu(100)

main()
