import random as rnd
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from itertools import islice

###########################
###BLOQUE DE GENERADORES###
###########################


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


def python_rand( num_iterations ):
     """
     Run the built-in python random number generator and output a number of data points
     specified by the user to a file
     :param num_iterations:  The number of data points to write to file
     :return: void
     """
     # Initialize seed value
     x_value = 123456789.0    # Our seed, or X_0 = 123456789
     rnd.seed(x_value)

     # counter for how many iterations we've run
     counter = 0

     # Open a file for output
     outFile = open("py_random_output.txt", "w")

     # Perform number of iterations requested by user
     while counter < num_iterations:
        x_value = rnd.random()
        # Write to file
        writeValue = str(x_value)
        outFile.write((writeValue + "\n"))
        counter = counter + 1

     outFile.close()
     print("Successfully stored" + str(num_iterations) + "random numbers in file named: 'py_random_output.txt'.")

####################
###BLOQUE DE TEST###
####################

# STATISTICAL TESTS
    # Check for uniformity at 80%, 90%, and 95% level. Note that some tests are one-sided, others two sided
    # x 1. Chi-Square Frequency Test for Uniformity
    #      - Collect 10,000 numbers per generation method
    #      - Sub-divide[0.1) into 10 equal subdivisions
    # x 2. Kolmogorov-Smirnov Test for uniformity
    #      - Since K-S Test works better with a smaller set of numbers, you may use the first 100
    #        out fo the 10,000 that you generated for the Chi-Square Frequency Test
    # x 3. Run Test for Independence
    #      - Use all 10,000 numbers per method for this test
    # x 4. Autocorrelations test for independence
    #      - Use all 10,000 numbers per method
    #      - Set of tests, but consider different parameterizations.
    #      - Experiment with diff gap sizes (param 1 in our notes): 2,3,5,50.
    #      - But don't consider different starting points (parameter i in our notes)
    #      - Simply choose one and specify what was used, in the report
    #      - Check these links to help implement: http://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm
    #      - http://www.aritzhaupt.com/resource/autocorrelation/


def chi_square_uniformity_test( data_set, confidence_level, num_samples ):
    """
    Null hypothesis:  Our numbers distributed uniformly on the interval [0, 1).

    This function uses the chi-square test for uniformity to determine whether our numbers
    are uniformly distributed on the interval [0,1).

    Formula is: "sum[ (observed-val - expected-val)^2 / expected val ], from 0 to num_samples"
    This gives us a number which we can test against a chi-square value table.

    Also need to know, degrees of freedom:  df=num_samples-1
    :param data_set: the data_set, must be a dictionary with 10 intervals.
                     Use return value from  @divide_RNG_data_into_10_equal_subdivisions_and_count
    :param confidence_level: confidence level we are testing at
    :param num_samples: number of data points
    :return: A chi-squared value
    """
    # This is our test statistic, this will be an accumulated value, as we loop through the data set
    chi_sq_value = 0.0
    degrees_of_freedom = num_samples - 1

    # We're doing 10 equal subdivisions, so need to divide our number samples by 10,
    # Assuming uniform distribution, to get an expected value. All values should be same
    # If our distro is actually uniform.
    expected_val = num_samples/10.0


    # Loop through a dictionary and get every count
    # The observed value is going to be our count at each key, and then we can do chi-square
    for observed_val in data_set:
        # print "Observed value is: " + observed_val
        chi_sq_value += ( pow((expected_val - data_set[observed_val]), 2)/expected_val )

    # Coming out of this loop, we'll have a chi-squared test statistic
    # Now we just need to do a lookup to see if it's valid
    print(chi_sq_value)
    return chi_sq_value

def divide_RNG_data_into_10_equal_subdivisions_and_count( data_file ):
    """
    Takes a path to a data file in the current directory.
    Returns a dictionary with keys 1-10, values=num instances in each of
    10 equal intervals from range: [0, 1).
    The function counts how many data points are in each interval, and gives us
    a dictionary so we can manipulate this data more easily, based on count by index.

    :param data_file: Must be in current directory. Pass in the string name.
    :return: A dictionary with counts of how many occurrences our data had for each
    of 10 equal intervals between [0, 1). (Divided into 10ths)
    """
    # For each of our uniformity tests, need to divide our data points in 10 equal subdivisions
    subdivisions = {  "1":  0,
                      "2":  0,
                      "3":  0,
                      "4":  0,
                      "5":  0,
                      "6":  0,
                      "7":  0,
                      "8":  0,
                      "9":  0,
                      "10": 0   }
    with open(data_file, "r") as f:
        # data points is a list containing all numbers we've read in.
        data_points = f.readlines()
    # Loop through our data points and count number of data points in each subdivision
    # Divide by tenths, from 0.0 to 1.0.
    for num in data_points:
        num = float(num)
        if num < 0.1:
            subdivisions["1"] += 1
        elif num < 0.2:
            subdivisions["2"] += 1
        elif num < 0.3:
            subdivisions["3"] += 1
        elif num < 0.4:
            subdivisions["4"] += 1
        elif num < 0.5:
            subdivisions["5"] += 1
        elif num < 0.6:
            subdivisions["6"] += 1
        elif num < 0.7:
            subdivisions["7"] += 1
        elif num < 0.8:
            subdivisions["8"] += 1
        elif num < 0.9:
            subdivisions["9"] += 1
        elif num < 1.0:
            subdivisions["10"] += 1
    
    #Bloque de ploteo
    a = []
    b = []
    for i in range(10):
        a.append(i+1)
        aux = str(i+1)
        b.append(subdivisions[aux])
    plt.bar(a,b)
    plt.show()

    return subdivisions

def chi_sq_significance_test( chi_sq, signif_level):
    """
    Performs a significance test for df=10000, based on values calculated at:
    https://stattools.crab.org/Calculators/chiSquareCalculator.htm
    :param chi_sq:  Chi-sq value to test
    :param signif_level: Level of significance we are testing: 0.80, 0.90, or 0.95
    :return: message stating whether we accept or reject null
    """
    result = "FAIL TO REJECT null hypothesis"
    crit_value = 0.0
    if signif_level == 0.8:
        crit_value = 10118.8246
    elif signif_level == 0.90:
        crit_value = 10181.6616
    elif signif_level == 0.95:
        crit_value = 10233.7489
    else:
        print ("**Invalid Significance Level for Chi Sq***")

    if chi_sq > crit_value:
        result = "REJECT null hypothesis"

    print ("Print Significance Level: " + str(signif_level))
    print ("Chi Sq: " + str(chi_sq))
    print ("Crit Value: " + str(crit_value))
    print ("Result is: " + result)
    print ("....................................")

    return result

def chitest(input_file, number_observations):
    
    # divide our output values in 10 equal subdivisions and run chi-square test
    print ("---------CHI-SQ_TEST-----------")
    data_points = divide_RNG_data_into_10_equal_subdivisions_and_count(input_file)
    chi_sq_result = chi_square_uniformity_test(data_points, 0, number_observations)
    chi_sq_significance_test( chi_sq_result, 0.8 )
    chi_sq_significance_test( chi_sq_result, 0.9 )
    chi_sq_significance_test( chi_sq_result, 0.95 )

    


def main():
    metodosCuadrados(10000)
    generate_gcl_rand(100)
    generate_gcl_randu(10000)
    python_rand(100)
    chitest("lgc_RANDU_output.txt", 10000)
    chitest("m2_output.txt",10000)

main()
