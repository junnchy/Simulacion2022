import math
import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import scipy.special as sps

def main():

    ng = 10000 #ng = numeros generados largo de los arreglos

    #uniforme
    array = []
    x = 0
    for i in range(ng):
        z = rnd.random()
        array.append(z)
        x += z
    prom = x/ng
    plt.hist(array,20)
    plt.xlabel('Intervalos de Datos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.axhline(y=prom, color='r', linestyle='-')
    plt.show()

    #exponencial
    exponencial(ng, 2)
    prueba_exp(ng, 2)

    #Gamma
    sum=0
    arr=[]
    for i in range(ng):
        num=distribucion_gamma(10000,0.5)
        arr.append(num)
    plt.hist(arr,20)
    plt.title('Distribucion Gamma con ' + ng + ' numeros generados')
    plt.xlabel('Intervalos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show()

    #Normal
    sum=0
    arr2=[]
    for i in range(ng):
        num=distribucion_normal(10,5)
        arr2.append(num)

    plt.hist(arr2,20)
    plt.show()

    #poison
    sum=0
    arr2=[]
    for i in range(ng):
        num=distribucion_poisson(2)
        arr2.append(num)
    plt.hist(arr2,20)
    plt.show()





def distribucion_uniforme(a, b, datos):
    #a y b son los valores de uniformidad
    aux = []
    for r in datos:
        aux.append(a + (b - a) * r)
    uniformidad(aux)

def uniforme(ng):
    array = []
    x = 0
    for i in range(ng):
        z = rnd.random()
        array.append(z)
        x += z
    prom = x/ng
    plt.hist(array,20)
    plt.xlabel('Intervalos de Datos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.axhline(y=prom, color='r', linestyle='-')
    plt.show()

def distr_exponencial(ex):
    r=np.random.rand()
    x=-ex*np.log(r)
    return x

def exponencial(ng, ex):
    sum=0
    arr=[]
    for i in range(ng):
        num=distr_exponencial(ex)
        arr.append(num)
        sum=sum+num
    plt.hist(arr,25)
    plt.title('Exponencial por funcion inversa')
    plt.xlabel('Intervalos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show() 

def distribucion_gamma(k, a):
    #a = EX
    tr= 1.0
    for i in range(k+1):
        r=np.random.rand()
        tr*=r
    x=-(np.log(tr))/a
    return x

def gamma(k,a):
    arr=[]
    for i in range(k+1):
        num = distribucion_gamma(k,a)
        arr.append(num)
    print(arr)
    plt.hist(arr,25)
    plt.title('Distribucion Gamma con ' + str(k) +' numeros generados')
    plt.xlabel('Intervalos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show()

def distribucion_normal(ex, stdx):
	suma = 0
	for i in range(12):
		suma += np.random.rand()
	return stdx * (suma - 6) + ex

def normal(ng, ex, stdx):
    arr2=[]
    for i in range(ng):
        num=distribucion_normal(ex,stdx)
        arr2.append(num)
    plt.hist(arr2,20)
    plt.title('D. Normal por funcion inversa')
    plt.xlabel('Intervalos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show()


def distribucion_pascal(k, q):
	tr = 1
	for i in range(k):
		tr *= np.random.rand()
	return math.log(tr) / math.log(q)


def distribucion_binomial(n, p):
	x = 0
	for i in range(n):
		r = np.random.rand()
		if (r - p) <= 0:
			x+=1
	return x

def binomial(ng, a, b):
    arr2=[]
    for i in range(ng):
        num=distribucion_binomial(a, b)
        arr2.append(num)
    plt.hist(arr2,20)
    plt.show()


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


def distribucion_poisson(p):
	x = 0
	b = math.exp(-p)
	tr = 1
	aux = True
	while aux:
		tr *= np.random.rand()
		if (tr - b) >= 0:
			x +=1
		else:
			aux = False
	return x

def poisson(ng, p):
    arr2=[]
    for i in range(ng):
        num=distribucion_poisson(p)
        arr2.append(num)
    plt.hist(arr2,20)
    plt.title('Poisson')
    plt.xlabel('Intervalos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show()


def generarValores01(cantidad):
    x = []
    y = []
    for i in range(cantidad):
        y.append(i)
        z = rnd.random()
        x.append(z)
    return [x,y]


def uniformidad( arreglo ):
    plt.hist(arreglo,20)
    plt.xlabel('Intervalos de Datos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show()

def img(a,b):
    plt.bar(a,b)
    plt.xlabel('Intervalos de Datos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show()


#--------------------PRUEBAS------------------------------
def prueba_exp(ng, ex):
    dt = np.random.exponential(ex, ng)
    _, bins, _ = plt.hist(dt, 25)
    y_curve = scipy.stats.expon.pdf(bins)
    plt.plot(y_curve, 'k')
    plt.title('Numpy Exponencial')
    plt.xlabel('Intervalos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show() 

def prueba_normal(ng, stdx, ex):
    dt = np.random.normal(ex, stdx, ng)
    _, bins, _ = plt.hist(dt, 20)
    y_curve = scipy.stats.norm.pdf(bins)
    plt.plot(y_curve, 'k')
    plt.title('Numpy Normal')
    plt.xlabel('Intervalos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show() 

def prueba_poisson(ng, lam):
    dt = np.random.poisson(lam, ng) 
    count, bins, ignored = plt.hist(dt, 20, density=True)
    plt.plot()  
    plt.title('Numpy Poisson')
    plt.xlabel('Intervalos')
    plt.ylabel('Cantidades de Datos por Intervalo')
    plt.show() 

def main2():
    poisson(1000, 10)
    prueba_poisson(1000,10)
    

main2()

