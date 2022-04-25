from ast import If
import random as rnd
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from itertools import islice


def main():
    

    #Metodo de los Cuadrados con test
    #metodosCuadrados(10000)
    #chitest("m2_output.txt",10000)
    #kstest("m2_output.txt")
    #test_de_independencia("m2_output.txt",10000)
    #test_de_autocorrelacion("m2_output.txt",10000)

    #Metodo de GCL Rand
    #generate_gcl_rand(10000)
    #chitest("lgc_rand_output.txt",10000)
    #kstest("lgc_rand_output.txt")
    #test_de_independencia("lgc_rand_output.txt",10000)
    #test_de_autocorrelacion("lgc_rand_output.txt",10000)

    #Metodo de GCL Randu
    generate_gcl_randu(10000)
    chitest("lgc_RANDU_output.txt",10000)
    kstest("lgc_RANDU_output.txt")
    test_de_independencia("lgc_RANDU_output.txt",10000)
    test_de_autocorrelacion("lgc_RANDU_output.txt",10000)

    #generate_gcl_rand(100)
    #generate_gcl_randu(10000)
    #python_rand(10000)
    #chitest("lgc_RANDU_output.txt", 10000)

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
        already_seen.add(number)
        number = int(str(number * number).zfill(8)[2:6])  # zfill adds padding of zeroes
        #print(f"#{counter}: {number}")
        aux = number/10000
        writeValue = str(aux)
        outFile.write(writeValue + "\n")
    
    outFile.close()

     
    """ print(f"Empezamos con{seed_number} y"
    f" el bloque se repite despues de {counter} pasos"
    f" con {number}.") """
   


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
    print("Se guardaron correctamente " + str(num_iterations) + " numeros aleatorios en el archivo: 'lgc_output.txt'.")


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
    print ("Se guardaron correctamente " + str(num_iterations) + " numeros aleatorios en el arechivo: 'lgc_RANDU_output.txt'.")


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
     print("Se guardaron correctamente" + str(num_iterations) + "numeros aleatorios en el arechivo: 'py_random_output.txt'.")

####################
###BLOQUE DE TEST###
####################

# TESTS ESTADISTICOS
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

#Tes de Chi2
def chitest(input_file, number_observations):
    
    # divide our output values in 10 equal subdivisions and run chi-square test

    if input_file == 'm2_output.txt':
        print ("---------CHI-SQ_TEST Metodo de los cuadrados----------")
    elif input_file == 'lgc_RANDU_output.txt':
        print ("---------CHI-SQ_TEST Metodo GCL RANDU-----------")
    elif input_file == 'lgc_rand_output.txt':
        print ("---------CHI-SQ_TEST Metodo GCL Rand ---------")
    else:
        print ("---------CHI-SQ_TEST-----------")

    data_points = divide_RNG_data_into_10_equal_subdivisions_and_count(input_file)
    chi_sq_result = chi_square_uniformity_test(data_points, 0, number_observations)
    chi_sq_significance_test( chi_sq_result, 0.8 )
    chi_sq_significance_test( chi_sq_result, 0.9 )
    chi_sq_significance_test( chi_sq_result, 0.95 )

    df = pd.DataFrame(list(data_points.items()),columns = ['numero','cantidad']) 

    print(df)

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

#Test de Kolmogorov Smirnov
def kstest(input_file):
    # get first 100 values from sample and run kolmogorov-smirnov test
    print ("---------KS_TEST-----------")
    first_100_values = collect_first_100_samples_in_data_set(input_file)
    first_100_values.sort()
    ks_result = kolmogorov_smirnov_test(first_100_values,1,100)
    ks_significance_test(ks_result,100, 0.1)
    ks_significance_test(ks_result,100, 0.05)
    ks_significance_test(ks_result,100, 0.01)
    print( "Kolmogorov-Smirnov Test Result for D-Value: " + str(ks_result))
    print ("")

def kolmogorov_smirnov_test( data_set, confidence_level, num_samples ):
    """
    Kolmogorov-Smirnov test for uniform distribution of Random numbers
    :param data_set: The set of data to analyze. Should be floating point numbers [0,1) in a .txt file
    :param confidence_level: with how much confidence should we test?
    :param num_samples: number of samples to analyze
    :return: test statistic
    """
    # Step 1:  Rank data from smallest to largest, such that:
    # R(1) <= R(2) <= R(3) ... <= R(i)
    data_set.sort()

    # Step 2: Computer D+ and D-
    # D+ = max(i/N - R(i))
    d_plus = get_d_plus_value_for_KS_TEST(data_set, num_samples)
    print ("D+ VALUE ="+str(d_plus))

    # D- = max(R(i) - (i -1)/n)
    d_minus = get_d_minus_value_for_KS_TEST(data_set, num_samples)
    print ("D- VALUE="+str(d_minus))

    # Step 3:  Computer D = max(D+,D-)
    d_value = max(d_plus, d_minus)
    print ("D VALUE (max): "+str(d_value))

    # Step 4: Determine critical value, using table
    # Step 5: Accept or reject Null hypothesis
    return d_value

#Test de Independencia
def test_de_independencia(input_file, number_observations):
    print ("---------RUNS_TEST-----------")
    runs_test_result = runs_test_for_independence( input_file, number_observations )
    print ("Resultado de ejecucion Z-Score: " + str(runs_test_result))
    print ("")
    z_score_lookup(runs_test_result, 0.8, two_sided=True)
    z_score_lookup(runs_test_result, 0.9, two_sided=True)
    z_score_lookup(runs_test_result, 0.95, two_sided=True)
    print ("")

def runs_test_for_independence( data_file, num_samples ):
    """
    Perform a runs test for independence for a set of random numbers
    :param data_set: A data set with 10,000 samples - should be a list, with all numbers floats
    :param num_samples: The number of samples to test
    :return: z-test statistic for our data set
    """
    # Note, every sequence begins and ends with "NO EVENT"
    # Run = Succession of similar events, followed by a different event
    # Run Length = Number of events that occur in the run
    # Number of runs = number of "runs" total
    # Two concerns: Num runs, length of runs
    # We're looking for:  Runs of larger and smaller numbers (increasing or decreasing)
    runLengths = { }       # The size of each run, in order
    numRuns = 0            # The number of runs overall
    runDirection = "none"  # We'll use "none", "up", and "down" to keep track

    with open( data_file, "r" ) as f:
        data_points = f.readlines()


   # for value in data_points:
    for value in range(0, (len(data_points)-1) ):

        # DEBUG
        thisValue = float(data_points[value])
        nextValue = float(data_points[value+1])
        # print "data_points[value] ::"+ str(thisValue)
        # print "dat_points[value+1] ::"+ str(nextValue)

        # If no change in direction we'll ignore
        if thisValue == nextValue:
            numRuns = numRuns             # numRums overall, doesn't change
            runDirection = runDirection   # runDirection doesn't change

        # Check if we have a NEW run, going UP
        elif thisValue < nextValue and runDirection != "up":
            numRuns = numRuns + 1         # We have a NEW run
            runDirection = "up"           # We have a NEW run direction
            runLengths[numRuns] = 1       # We have a NEW key in our dictionary, with value=1

        # Check if we have a CONTINUING run, going UP
        elif thisValue < nextValue and runDirection == "up":
            runLengths[numRuns] += 1      # increment the run length in our dictionary for current run
                                          # NumRuns doesn't change
                                          # runDirection doesn't change

        # Check if we have NEW run, going DOWN
        elif thisValue > nextValue and runDirection != "down":
            numRuns = numRuns + 1          # We have a NEW run
            runDirection = "down"          # We have a NEW run direction
            runLengths[numRuns] = 1        # We have a NEW key in our dictionary, with value=1

        # Check if we have a CONTINUING run, going DOWN
        elif thisValue > nextValue and runDirection == "down":
            runLengths[numRuns] += 1      # increment the run length in our dictionary for current run
                                          # NumRuns doesn't change
                                          # runDirection doesn't change

    # Leaving this loop, we should have a dictionary with our run numbers mapped to their lengths
    # We should also have a the number of runs

    # Now, calculate mean:  Mean = (2N-1)/3
    mean =  ( (2*num_samples - 1) / 3 )

    # And variance:  Variance = (16(N) - 29) / 90
    variance = ( ( 16*num_samples - 29) / 90 )

    # And we can use the mean & variance to calculate the Z-Test statistic
    z_statistic = ( (numRuns - mean) / np.sqrt(variance) )

    print ("Numero de Ejecuciones: " + str(numRuns)+ " \\")

    return z_statistic

#Test de Autocorrelacion
def test_de_autocorrelacion(input_file,number_observations):
    print ("---------TEST DE AUTOCORRELACION-----------\\")
    auto_test_result = autocorrelation_tests(input_file, number_observations, 2 )
    print ("==== Resutado de test de autocorrelacion para el tamaño de espacio=2: " + str(auto_test_result)+ " \\")

    z_score_lookup(auto_test_result, 0.8, two_sided=True)
    z_score_lookup(auto_test_result, 0.9, two_sided=True)
    z_score_lookup(auto_test_result, 0.95, two_sided=True)
    print ("")
    print ("       ===== FIN TAMAÑO DE ESPACIO =2 ===== \\")
    print ("")
    print ("")
    auto_test_result = autocorrelation_tests(input_file, number_observations, 3 )
    print ("=== Resutado de test de autocorrelacion para el tamaño de espacio=3: " + str(auto_test_result)+ " \\")
    z_score_lookup(auto_test_result, 0.8, two_sided=True)
    z_score_lookup(auto_test_result, 0.9, two_sided=True)
    z_score_lookup(auto_test_result, 0.95, two_sided=True)
    print ("")
    print ("       ===== FIN TAMAÑO DE ESPACIO=3 =====\\")
    print ("")
    print ("")
    auto_test_result = autocorrelation_tests(input_file, number_observations, 5 )
    print (" === Resutado de test de autocorrelacion para el tamaño de espacio=5: " + str(auto_test_result)+ " \\")
    z_score_lookup(auto_test_result, 0.8, two_sided=True)
    z_score_lookup(auto_test_result, 0.9, two_sided=True)
    z_score_lookup(auto_test_result, 0.95, two_sided=True)
    print ("")
    print ("       ===== FIN TAMAÑO DE ESPACIO=5 =====\\")
    print ("")
    print ("")
    auto_test_result = autocorrelation_tests(input_file, number_observations, 50 )
    print ("Resutado de test de autocorrelacion para el tamaño de espacio=50: " + str(auto_test_result)+ " \\")
    z_score_lookup(auto_test_result, 0.8, two_sided=True)
    z_score_lookup(auto_test_result, 0.9, two_sided=True)
    z_score_lookup(auto_test_result, 0.95, two_sided=True)
    print ("")
    print ("       ===== FIN TAMAÑO DE ESPACIO=50 ===== \\")
    print ("")
    print ("")
    print ("")
    print ("=-=-=-======= END TEST SUITE ======-=-=-=-= \\")
    print ("")

def autocorrelation_tests( data_file, num_samples, gap_sequence ):
    """
    This function performs an autocorrelation test
    :param data_file:  The data set to analyze. Should be 10,000 samples, all floats, in a .txt file
    :param num_samples:  The number of samples to analyize
    :return: The test result
    """

    # Get necesssary values, store in "data_points" list
    with open( data_file, "r" ) as f:
         data_points = f.readlines()

    # Sort data set
    # data_points.sort()

    little_m = gap_sequence    # The space between the numbers being tested
    ###### CHANGE BACK TO 0 #########
    start_index = 0            # The number in the sequence we start with
    ########### end #################
    big_n = num_samples        # the number of numbers generated in a sequence
    big_m = 0.0                  # Largest number such that i + (M+1)m <= N

    # Determine correct M value
    while (big_m + 1) < ( (big_n - start_index)/little_m ) :
        big_m = big_m + 1

    # print "Final value for big_m: " + str(big_m)

    one_over_m_plus_one = ( 1.0/(big_m + 1.0 ) )
    rho_hat = 0.0
    sum_of_rho_hat = 0.0


    # Get every m'th element in the data_set
    every_m_element = data_points[0::gap_sequence]

    # print "Length: " + str(len(every_m_element))
    # Get the sum of rho_hat
    for value in range(0, (len(every_m_element)-1) ):
        thisValue = float(every_m_element[value])
        nextValue = float(every_m_element[value+1])
        # print "Autocorrelation: Ki   :" + str(thisValue)
        # print "Autocorrelation: Ki+1 :" + str(nextValue)
        sum_of_rho_hat = sum_of_rho_hat + (thisValue * nextValue)
        # print "Sum of rho hat: " + str(sum_of_rho_hat)

    # Subtract 0.25
    sum_of_rho_hat = (one_over_m_plus_one * sum_of_rho_hat) - 0.25

    variance_of_rho =  np.sqrt( (13*big_m + 7 )) / (12*(big_m + 1))

    z_statistic = sum_of_rho_hat / variance_of_rho

    # print "Z-Score for autocorrelation is: " + str(z_statistic)
    return z_statistic

############################
###TESTS DE SIGNIFICANCIA###
############################

def chi_sq_significance_test( chi_sq, signif_level):
    """
    Performs a significance test for df=10000, based on values calculated at:
    https://stattools.crab.org/Calculators/chiSquareCalculator.htm
    :param chi_sq:  Chi-sq value to test
    :param signif_level: Level of significance we are testing: 0.80, 0.90, or 0.95
    :return: message stating whether we accept or reject null
    """
    result = "Aprueba la Hipotesis Nula"
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
        result = "Se Rechaza la Hipotesis Nula"

    print ("Print Significance Level: " + str(signif_level)+ " \\")
    print ("Chi Sq: " + str(chi_sq)+ " \\")
    print ("Valor Critico: " + str(crit_value)+ " \\")
    print ("Resultado: " + result+ " \\")
    print ("....................................\\")

    return result

def ks_significance_test( d_statistic, num_observations, alpha_level ):
    """
    Perform Significance test for Kolmogorov-Smirnov
    Uses formulas from table A.7:  Discrete-Event System Simulation, by Banks and Carson, 1984
    :param d_statistic: The d-value we are testing
    :param num_observations: The number of observations in our data set
    :param alpha_level: The level of significance we are testing
    :return: result -- accept or reject
    """
    result = "Aprueba la Hipotesis Nula"
    critical_value = 0


    if alpha_level == 0.1:
        critical_value = 1.22/np.sqrt(num_observations)
    elif alpha_level == 0.05:
        critical_value = 1.36/np.sqrt(num_observations)
    elif alpha_level == 0.01:
        critical_value = 1.63/np.sqrt(num_observations)
    else:
        print ("Nivel de Alpha invalido para el KS test. Debe ser: 0.1, 0.05, o 0.01")

    if d_statistic > critical_value:
        result = "Se rechaza la Hipotesis Nula"
    print ("Alpha Level: " + str(alpha_level)+ " \\")
    print ("D_statistic: " + str(d_statistic)+ " \\")
    print ("Valor Critico: " + str(critical_value)+ " \\")
    print ("Resultado: " + result+ " \\")
    print ("............................\\")

    return result

def z_score_lookup( z_score, significance_level, two_sided=True):
    """
    Performs a two-sided z-score lookup, for 0.8, 0.9, or 0.95 level of significance
    :param z_score: Z score to test
    :param significance_level: Significance level
    :return: String detailing our result
    """

    result = "Aprueba la Hipotesis Nula"
    critical_value = 0.0
    confidence_80 = 1.282
    confidence_90 = 1.645
    confidence_95 = 1.96
    confidence_99 = 2.576

    # Assign confidence interval z-scores to our crit value
    if significance_level == 0.8:
        critical_value = confidence_80
    elif significance_level == 0.9:
        critical_value = confidence_90
    elif significance_level == 0.95:
        critical_value = confidence_95
    else:
        print ("Invalid significance level for z-lookup. Must be: 0.8, 0.9, or 0.95")

    # Need to adjust intervals if the test is one sided
    if two_sided == False:
        if critical_value == confidence_80:
            critical_value = 0.8416
        elif critical_value == confidence_90:
            critical_value = 1.282
        elif critical_value == confidence_95:
            critical_value = 1.645



    neg_crit_value = critical_value * (-1.0)

    #if z_score < 0:
     #  z_score = z_score * (-1)

    if ( two_sided and ( z_score <= neg_crit_value) or (critical_value <= z_score ) ):
        result = "Se Rechaza la Hipotesis Nula \\"

    if ( not two_sided and z_score >= critical_value or z_score <= neg_crit_value):
        result = "Se Rechaza la Hipotesis Nula \\"

    print ("Z score es: " + str(z_score)+ " \\")
    print ("Significance level is: " + str(significance_level)+ " \\")
    print ("Critical value is: " +str(critical_value)+ " \\")
    #print ("Running two sided z-score lookup? -->" + str(two_sided))
    #print ("")
    print ("El resultado es: " + result+ " \\")
    print ("..................................... \\")

    return result

##########################
###FUNCIONES DE SOPORTE###
##########################


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
    bm2 =[]
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
            bm2.append(1)
        elif num < 0.2:
            subdivisions["2"] += 1
            bm2.append(2)
        elif num < 0.3:
            subdivisions["3"] += 1
            bm2.append(3)
        elif num < 0.4:
            subdivisions["4"] += 1
            bm2.append(4)
        elif num < 0.5:
            subdivisions["5"] += 1
            bm2.append(5)
        elif num < 0.6:
            subdivisions["6"] += 1
            bm2.append(6)
        elif num < 0.7:
            subdivisions["7"] += 1
            bm2.append(7)
        elif num < 0.8:
            subdivisions["8"] += 1
            bm2.append(8)
        elif num < 0.9:
            subdivisions["9"] += 1
            bm2.append(9)
        elif num < 1.0:
            subdivisions["10"] += 1
            bm2.append(10)

    print('Nombre del archivo:', data_file)
    
    #Bloque de ploteo
    a = []
    b = []
    for i in range(10):
        a.append(i+1)
        aux = str(i+1)
        b.append(subdivisions[aux])
    plt.bar(a,b)
    if data_file == 'm2_output.txt':
        plt.title('Distribucion de Uniformidad Metodo de los cuadrados')
    elif data_file == 'lgc_RANDU_output.txt':
        plt.title('Distribucion de Uniformidad Metodo GCL RANDU')
    elif data_file == 'lgc_rand_output.txt':
        plt.title('Distribucion de Uniformidad Metodo GCL Rand')
    plt.xlabel('Intervalos de Datos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show()

    return subdivisions

def get_d_plus_value_for_KS_TEST( data_set, num_samples ):
    """
    Finds the D+ value for a KS test
    :param data_set: 100 values, must be a list of floats
    :return: the D-+Statistic for our data set
    """
    # D+ = max(i/N - R(i))
    d_plus_max = 0
    value_rank_i = 1

    # iterate through data set
    for value in data_set:
        # Do each D+ calculation, store it
        d_plus_i_value = ( (value_rank_i/num_samples) - value )

        # Check if it is highest D+ value yet
        if d_plus_i_value > d_plus_max:
            d_plus_max = d_plus_i_value

        # increment our "i" value
        value_rank_i = value_rank_i + 1

    # coming out of this loop, D+ = highest D+ value
    return d_plus_max

def get_d_minus_value_for_KS_TEST( data_set, num_samples ):
    """
    Finds the D- value for a KS test
    :param data_set: 100 values, must be a list of floats
    :return: the D- Statistic for our data set
    """
    # D- = max(R(i) - (i -1)/n)
    d_minus_max = 0
    value_rank_i = 1.0

    # iterate through data set
    for value in data_set:
        # Do each D+ calculation, store it
        substraction_value = ( (value_rank_i - 1.0)/num_samples )
        d_minus_i_value = value - substraction_value

        # Check if it is highest D+ value yet
        if d_minus_i_value > d_minus_max:
            d_minus_max = d_minus_i_value

        # increment our "i" value
        value_rank_i = value_rank_i + 1

    # coming out of this loop, D+ = highest D+ value
    return d_minus_max

def collect_first_100_samples_in_data_set( data_file ):
    """
    Takes a data file, with real number data points between [0,1) reads the first 100 values,
    then adds them to a dictionary as our return value
    :param data_file: A string - the name of the file to read in our current directory
    :return: A dictionary containing the first 100 values as floats
    """

    first_100_vals_as_FLOATS = []
    # grabs first 100 files, as strings with newline endpoints
    with open( data_file, "r" ) as f:
        first_100_vals_as_STRINGS = list(islice(f, 100))

    # transform all values to floats
    for val in first_100_vals_as_STRINGS:
        val = float(val)
        first_100_vals_as_FLOATS.append(val)

    return first_100_vals_as_FLOATS

main()
