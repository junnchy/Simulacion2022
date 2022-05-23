from ast import While
import random as rnd
import numpy as np


def main():
    #listado de variables
    estado_servidor = 0
    reloj = 0
    lista_de_eventos = [] #(tipo, reloj, subindice dentro de lista) tipo = [a,d,l] a = arribo, d = salida, l = libre
    evento_actual = ['l',0,0] #el que esta siendo atendido
    cola =  []
    prox= {
        'a': ('a', 0, 0), #(tipo ,tiempo, subindice))
        'd': ('d', 999999,0)

    }
    q_t = 0
    b_t = 0
    demora_total = 0
    cli_comp_dem_cola = 0
    num_cli_cola = 0
    sig_ev = 0
    relojarr = []
    i = 0

    lista_de_eventos.append(evento_actual)
    
    
    #while i < 2:
    for i in range(5):
        reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr = timing_routine(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr)
        reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr = event_routine(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr)

        print('reloj ',reloj)
        #print('Arreglo reloj: ', relojarr)
        #print(lista_de_eventos)
        print('evento actual ', evento_actual)
        print('estado del servidor', estado_servidor)
        print('Prox ', prox)
        print('eventos en cola ', cola)
        print('numeros de clientes en cola', num_cli_cola)
        print('clientes que completaron su demora en cola', cli_comp_dem_cola)
        print('Demora total: ', demora_total)
        print('b(t): ', b_t)
        print('q(t): ', q_t)
        print('------------------------------------------------------------------------')
    #i += 1
    

def timing_routine(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr):
    if reloj == 0:
        r = genera_random()
        x=-0.70*np.log(r) + reloj
        ev = ['a', x, len(lista_de_eventos)]
        lista_de_eventos.append(ev)
        reloj = x
        evento_actual = ev
        estado_servidor = 1
        sig_ev = 'a'
        cli_comp_dem_cola = 1
    else:
        relojarr.append([reloj,num_cli_cola])
        #el proximo evento es un arribo
        if prox['a'][1] < prox['d'][1]: 
            reloj = prox['a'][1]
            sig_ev = 'a'
        #el proximo evento es una partida
        else: 
            reloj = prox['d'][1]
            sig_ev = 'd'
    return reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr

def event_routine(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr):
    if str(evento_actual[0]) != 'l':
        if str(sig_ev) == 'a': #evento arribo
            reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr = evento_arribo(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr)
        else: #evento partida
            reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr =  evento_partida(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr)
    return reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr


def evento_arribo(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr):
    print('Ejecutando Arribo')
    r = genera_random()
    x=-0.70*np.log(r) + reloj
    ev = ['a', x, len(lista_de_eventos)]
    lista_de_eventos.append(ev)
    if estado_servidor == 1:
        if prox['a'][1] == 0: #No hay un proximo evento, usualmente solo funciona para la primer corrida
            prox['a'] = ev
        elif reloj == prox['a'][1]:
            cola.append(prox['a'])
            prox['a'] = ev #dudo de esta sentencia, me parece que lo debe hacer el timing routine
            num_cli_cola = len(cola)
        if prox['d'][1] == 999999:
            r = genera_random()
            x=-0.66*np.log(r) + reloj
            ev = ['d', x, len(lista_de_eventos)]
            lista_de_eventos.append(ev)
            prox['d'] = ev
        """ if len(cola) <= 1:
            b_t += (reloj-evento_actual[1])*estado_servidor
        else:
            b_t +=(reloj - cola[-1][1])*estado_servidor """
        if len(relojarr)!= 0:
            if len(cola) != 0:
                b_t += (reloj-relojarr[-1][0])*estado_servidor
                if num_cli_cola == relojarr[-1][1]:
                    q_t += (reloj-relojarr[-1][0])*num_cli_cola
                else:
                    q_t += (reloj-relojarr[-1][0])*relojarr[-1][1]
            
    else: #El arribo encuentra al servidor desocupado
        cli_comp_dem_cola += 1
        evento_actual = prox['a']
        estado_servidor = 1
        prox['a'] = ev
        if prox['d'][1] == 999999:
            r = genera_random()
            x=-0.66*np.log(r) + reloj
            ev = ['d', x, len(lista_de_eventos)]
            lista_de_eventos.append(ev)
            prox['d'] = ev
    return reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr

def evento_partida(reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr):
    print('Ejecutando Partida')
    if len(relojarr)!= 0:
            b_t += (reloj-relojarr[-1][0])*estado_servidor
            if num_cli_cola == relojarr[-1][1]:
                q_t += (reloj-relojarr[-1][0])*num_cli_cola
    if len(cola) == 0:
        estado_servidor = 0
        prox['d'] = ('d', 999999,0)
    else:
        aux = evento_actual
        evento_actual = cola[0]
        cli_comp_dem_cola += 1
        cola = cola[1:len(cola)]
        demora_total = reloj - evento_actual[1]
        num_cli_cola = len(cola)
        r = genera_random()
        x=-0.66*np.log(r) + reloj
        ev = ['d', x, len(lista_de_eventos)]
        lista_de_eventos.append(ev)
        prox['d'] = ev
        """ if len(cola) == 0:
            b_t +=(reloj - aux[1])*estado_servidor
        else: 
            b_t +=(reloj - cola[-1][1])*estado_servidor """
    return reloj, lista_de_eventos, evento_actual, estado_servidor, cola, prox, num_cli_cola, sig_ev, cli_comp_dem_cola, demora_total, q_t, b_t, relojarr
    
def genera_random():
    r = rnd.random()
    return r

def genera_partida():
    pass
def genera_arrbo():
    pass


main()