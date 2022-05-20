from ast import While
import random as rnd
import numpy as np


def main():
    #listado de variables
    estado_servidor = 0
    reloj = 0
    lista_de_eventos = [] #(tipo, reloj, subindice dentro de lista) tipo = [a,d,l] a = arribo, d = salida, l = libre
    evento_actual = ['l',0,0]
    cola =  []
    prox= {
        'a': ('a', 0, 0), #(tipo ,tiempo, subindice))
        'd': ('d', 999999,0)

    }
    q_t = []
    b_t = []
    i = 0

    lista_de_eventos.append(evento_actual)

    
    #while i < 2:
    for i in range(3):
        reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox = timing_routine(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox)
        reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox = event_routine(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox)
        print('reloj ',reloj)
        print(lista_de_eventos)
        print('evento actual ', evento_actual)
        print('eventos en cola ', cola)
        print('Prox ', prox)
        print('------------------------------------------------------------------------')
    #i += 1
    

def timing_routine(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox):
    if reloj == 0:
        r = genera_random()
        x=-0.70*np.log(r) + reloj
        ev = ['a', x, len(lista_de_eventos)]
        lista_de_eventos.append(ev)
        reloj = x
        evento_actual = ev
        estado_servidor = 1
    else:
        #el proximo evento es un arribo
        if prox['a'][1] < prox['d'][1]: 
            evento_actual = prox['a']
            reloj = prox['a'][1]
            if estado_servidor == 1:
                cola.append(prox['a'])
                #hacer variable num de cliente en cola ncc = len(cola+1)

        #el proximo evento es una partida
        else: 
            evento_actual = prox['d']
            reloj = prox['d'][1]
    return reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox

def event_routine(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox):
    print(evento_actual)
    if str(evento_actual[0]) != 'l':
        if str(evento_actual[0]) == 'a':
            reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox = evento_arribo(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox)
        else: #evento partida
            reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox =  evento_salida(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox)
    
    return reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox


def evento_arribo(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox):
    print('Ejecuntando Arribo')
    r = genera_random()
    x=-0.70*np.log(r) + reloj
    ev = ['a', x, len(lista_de_eventos)]
    lista_de_eventos.append(ev)
    if estado_servidor == 1:
        #cola.append(ev)
        if prox['a'][1] == 0:
            prox['a'] = ev
        elif reloj == evento_actual[1]:
            prox['a'] = ev
        if prox['d'][1] == 999999:
            r = genera_random()
            x=-0.66*np.log(r) + reloj
            ev = ['d', x, len(lista_de_eventos)]
            lista_de_eventos.append(ev)
            prox['d'] = ev
        else:
            pass
    else: #El arribo encuentra al servidor desocupado
        pass
    return reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox

def evento_salida(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox):
    print('Ejecutando Partida')
    return reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox
    


def genera_random():
    r = rnd.random()
    return r


main()