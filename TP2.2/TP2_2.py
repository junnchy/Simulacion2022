import math
import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats



def main():

    ng = 10000 #ng = numeros generados

    #uniforme
    array = generarValores01(ng)[0]
    plt.hist(array,20)
    plt.xlabel('Intervalos de Datos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show()

    #exponencial
    sum=0
    arr=[]
    for i in range(ng):
        num=distr_exponencial(10)
        arr.append(num)
        sum=sum+num
    plt.hist(arr,25)
    plt.show() 
    pruebaexp()

    #Gamma
    sum=0
    arr=[]
    for i in range(10000):
        num=distribucion_gamma(10000,50)
        arr.append(num)

    plt.hist(arr,20)
    plt.show()

    #Normal
    sum=0
    arr2=[]
    for i in range(10000):
        num=distribucion_normal(10,5)
        arr2.append(num)

    plt.hist(arr2,20)
    plt.show()

    #Pascal
    sum=0
    arr2=[]
    for i in range(10000):
        num=distribucion_pascal(10,2)
        arr2.append(num)

    plt.hist(arr2,20)
    plt.show()






def distribucion_uniforme(a, b, datos):
    #a y b son los valores de uniformidad
    aux = []
    for r in datos:
        aux.append(a + (b - a) * r)
    uniformidad(aux)

def distr_exponencial(ex):
    r=np.random.rand()
    x=-ex*np.log(r)
    return x


def distribucion_exponencial(rnd, ex):
	r = rnd()
	return -ex * (math.log(r))

#REVISAR
def distribucion_gamma(k, a):
    tr=1.0
    for i in range(1,k):
        #r=distr_exponencial(10)
        r=np.random.rand()
        tr= tr*r
    x=-(np.log(r))/a
    return x

def distribucion_normal(ex, stdx):
	suma = 0
	for i in range(12):
		suma += np.random.rand()
	return stdx * (suma - 6) + ex


def distribucion_pascal(k, q):
	tr = 1
	for i in range(k):
		tr *= np.random.rand()
	return math.log(tr) / math.log(q)


def distribucion_binomial(rnd, n, p):
	x = 0
	for i in range(n):
		r = rnd()
		if (r - p) <= 0:
			x+=1
	return x


def distribucion_hipergeometrica(rnd,tn, ns, p):
	x = 0
	for i in range(ns):
		r = rnd()
		if (r - p) > 0:
			s = 0
		else:
			s = 1
			x += 1
		p = (tn * p - s) / (tn - 1)
		tn -= 1
	return x


def distribucion_poisson(rnd, p):
	x = 0
	b = math.exp(-p)
	tr = 1
	aux = True
	while aux:
		tr *= rnd()
		if (tr - b) >= 0:
			x +=1
		else:
			aux = False
	return x

def varianza():
    pass
def esperanza():
    pass

def generarValores01(cantidad):
    x = []
    y = []
    for i in range(cantidad):
        y.append(i)
        z = rnd.random()
        x.append(z)
    return [x,y]


def uniformidad( arreglo ):
    bm2 =[]
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
    for num in arreglo:
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
    a = []
    b = []        
    for i in range(10):
        a.append(i+1)
        aux = str(i+1)
        b.append(subdivisions[aux])
    plt.hist(arreglo,20)
    plt.xlabel('Intervalos de Datos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show()

def img(a,b):
    plt.bar(a,b)
    plt.xlabel('Intervalos de Datos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show()


def prueba():
    # Importing the necessary libraries
    from matplotlib import pyplot as plt
    import numpy as np
    import scipy.stats

    dt = np.random.normal(0, 1, 1000)

    # Plotting the sample data on histogram and getting the bins
    _, bins, _ = plt.hist(dt, 25, density=1, alpha=0.5)


    # Getting the mean and standard deviation of the sample data dt
    mn, std = scipy.stats.norm.fit(dt)


    # Getting the best fit curve y values against the x data, bins
    y_curve = scipy.stats.norm.pdf(bins, mn, std)

    # Plotting the best fit curve
    plt.plot(bins, y_curve, 'k')

    plt.title('Best fit curve for histogram')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()

def pruebaexp():
    # Importing the necessary libraries
    from matplotlib import pyplot as plt
    import numpy as np
    import scipy.stats

    dt = np.random.exponential(10, 10000)

    # Plotting the sample data on histogram and getting the bins
    _, bins, _ = plt.hist(dt, 25, density=1, alpha=0.5)


    # Getting the mean and standard deviation of the sample data dt
    mn, std = scipy.stats.norm.fit(dt)


    # Getting the best fit curve y values against the x data, bins
    y_curve = scipy.stats.norm.pdf(bins, mn, std)

    # Plotting the best fit curve
    plt.plot(y_curve, 'k')

    plt.title('Best fit curve for histogram')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()   


main()