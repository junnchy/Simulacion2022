from random import randint
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from matplotlib.pyplot import figure


class Ruleta(object):

    def __init__(self):
        # Los arreglos terminados en A son arreglos de arreglos
        self.resultados = []
        self.apuestas = []
        self.ganadores = {}
        self.listaGanadores = []
        self.tiradas = []
        self.paga2 = ['par', 'impar', 'm-1', 'm-2', 'rojo', 'negro']
        self.paga1_5 = ['c-1', 'c-2', 'c-3', 'd-1', 'd-2', 'd-3']
        self.pagos = []
        self.panio = {
            'paridad': {
                'par': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36],
                'impar': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
            },
            'mitades': {
                '1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                '2': [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
            },
            'color': {
                'rojo': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
                'negro': [2, 4, 5, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
            },
            'docenas': {
                '1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                '2': [13, 14, 15, 16, 17, 18, 9, 20, 21, 22, 23, 24],
                '3': [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
            },
            'columnas': {
                '1': [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
                '2': [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                '3': [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
            },
        }

    def jugar(self, n):
        self.definirGanador(self.tirar(n))

    def tomarApuestas(self, apuestas):
        if apuestas == [None]:
            self.apuestas = []
        else:
            self.apuestas = []
            for apuesta in apuestas:
                self.apuestas.append(apuesta)

    def tirar(self, n):
        x = randint(0, 36)
        self.resultados.append(x)
        self.tiradas.append(n)
        return x

    def definirGanador(self, nro):
        ganadores = []
        if nro == 0:
            ganadores.append(nro)
        else:
            # Paridad
            if nro in self.panio['paridad']['par']:
                ganadores.append('par')
            elif nro in self.panio['paridad']['impar']:
                ganadores.append('impar')

            # Mitades
            if nro in self.panio['mitades']['1']:
                ganadores.append('m-1')
            elif nro in self.panio['mitades']['2']:
                ganadores.append('m-2')

            # Colores
            if nro in self.panio['color']['rojo']:
                ganadores.append('rojo')
            elif nro in self.panio['color']['negro']:
                ganadores.append('negro')

            # Docenas
            if nro in self.panio['docenas']['1']:
                ganadores.append('d-1')
            elif nro in self.panio['docenas']['2']:
                ganadores.append('d-2')
            elif nro in self.panio['docenas']['3']:
                ganadores.append('d-3')

            # Columnas
            if nro in self.panio['columnas']['1']:
                ganadores.append('c-1')
            elif nro in self.panio['columnas']['2']:
                ganadores.append('c-2')
            elif nro in self.panio['columnas']['3']:
                ganadores.append('c-3')

            self.ganadores = ganadores
            self.listaGanadores.append(ganadores)

    def devolverGanadores(self):
        return [self.listaGanadores, self.tiradas]
    
    def pagar(self):
        self.pagos = []
        if self.apuestas is not None:
            for apuesta in self.apuestas:
                if apuesta['apuesta'] in self.ganadores:
                    if apuesta['apuesta'] in self.paga2:
                        aux = apuesta['cantidad'] * 2
                        self.pagos.append({'pago': aux, 'nombre': apuesta['nombre']})
                    elif apuesta['apuesta'] in self.paga1_5:
                        aux = apuesta['cantidad'] * 1.5
                        self.pagos.append({'pago': aux, 'nombre': apuesta['nombre']})
                else:
                    self.pagos.append({'pago': 0, 'nombre': apuesta['nombre']})
            return self.pagos
        else:
            pass
            # print('No se recibieron apuestas')


class Jugador(object, ):

    def __init__(self, nombre, tc, jugada, aque):
        self.capital = 1000
        self.nombre = nombre
        self.apuesta = 1
        self.evolucionCapital = []
        self.ganancias = []
        self.resultados = []
        self.apuestas = []
        self.nroJuego = []
        self.ganadoxt = []
        self.ganados = 0
        self.perdidos = 0
        self.jugada = jugada
        self.aque = aque #Variable que define la jugada --> 1-Martingala; 2-Dalembert
        self.tc = tc  # Tipo de capital 0 limitado 1 ilimitado
        self.juega = True
        self.j = 0

    def continua(self):
        return self.juega

    def defineJuagda(self):
        if self.jugada == 1:
            return self.apostarMartingala(self.aque)
        if self.jugada == 2:
            return self.apostarDalambert(self.aque)
        

    def apostarMartingala(self, valor):
        if self.nroJuego == []:
            self.j += 1
            self.nroJuego.append(self.j)
            self.capital -= self.apuesta
            self.apuestas.append(self.apuesta)
            return {
                'apuesta': valor,
                'cantidad': self.apuesta,
                'nombre': self.nombre
            }
        else:
            if self.resultados[-1] == 'perdi':
                self.apuesta = self.apuesta * 2
            else:
                pass
            if self.capital >= self.apuesta:
                self.j += 1
                self.nroJuego.append(self.j)
                self.capital -= self.apuesta
                self.apuestas.append(self.apuesta)

                return {
                    'apuesta': valor,
                    'cantidad': self.apuesta,
                    'nombre': self.nombre
                }
            else:
                # print('Ya no queda plata')
                self.juega = False

    def apostarDalambert(self, valor):
        if self.nroJuego == []:
            self.j += 1
            self.nroJuego.append(self.j)
            self.capital -= self.apuesta
            self.apuestas.append(self.apuesta)
            return {
                'apuesta': valor,
                'cantidad': self.apuesta,
                'nombre': self.nombre
            }
        else:
            if self.resultados[-1] == 'perdi':
                self.apuesta = self.apuesta + 1
            else:
                pass
            if self.capital >= self.apuesta:
                self.j += 1
                self.nroJuego.append(self.j)
                self.capital -= self.apuesta
                self.apuestas.append(self.apuesta)

                return {
                    'apuesta': valor,
                    'cantidad': self.apuesta,
                    'nombre': self.nombre
                }
            else:
                # print('Ya no queda plata')
                self.juega = False


    def tomarGanancia(self, ganancia):
        for pago in ganancia:
            if pago['nombre'] == self.nombre:
                if pago['pago'] == 0:
                    self.resultados.append('perdi')
                    self.perdidos += 1
                    if self.tc == 1:
                        self.capital = self.capital * 2  # Capital limitado
                    else:
                        pass
                else:
                    self.capital = (self.capital) + pago['pago']
                    self.resultados.append('gane')
                    self.ganados += 1
                self.ganancias.append(pago['pago'])
                self.evolucionCapital.append(self.capital)
                # self.mostarResultados()
            else:
                pass

    def mostarResultados(self):
        print('Resultados: ', self.resultados)
        print('Ganancias: ', self.ganancias)
        print('Apuestas: ', self.apuestas)
        print('1...', self.nroJuego)
        print('Ganados:', self.ganados)
        print('Perdidos', self.perdidos)


    def devolverResultados(self):
        if self.tc == 1:
            return [self.apuestas, self.ganancias, self.nroJuego, [self.ganados, self.perdidos]]
        else:
            return [self.apuestas, self.ganancias, self.nroJuego, [self.ganados, self.perdidos], self.evolucionCapital]

    def sayName(self):
        if self.jugada == 1:
            return self.nombre, 'Martingala', self.aque
        if self.jugada == 2:
            return self.nombre, 'Dalambert', self.aque

    def sayNombre(self):
        return self.nombre

    def imprimirGraficos(self):
        print(len(self.nroJuego), self.nroJuego)
        print(len(self.evolucionCapital), self.evolucionCapital)
        print(len(self.apuestas), self.apuestas)

        plt.subplot(2, 2, 1)
        plt.plot(self.nroJuego, self.apuestas, color='darkblue')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('Apuestas')

        plt.subplot(2, 2, 2)
        plt.plot(self.nroJuego, self.ganancias, color='darkblue')
        plt.xlabel('n (numero de tiradas)')
        plt.ylabel('Ganancias')

        plt.show()


def armadataFrame(datos):
    datosganadores = []
    aux = datos[1]

    fr_porvuelta = []

    fr_par = 0
    fr_impar = 0
    fr_negro = 0
    fr_rojo = 0
    fr_m1=0
    fr_m2=0
    fr_d1=0
    fr_d2=0
    fr_d3=0
    
    for g in range(len(datos[0])):
        if datos[0][g][0] == 'impar':
            fr_impar = fr_impar + 1
        else:
            fr_par = fr_par + 1 

        if datos[0][g][1] == 'm-1':
            fr_m1 = fr_m1 + 1
        elif datos[0][g][1] == 'm-2':
            fr_m2 = fr_m2 + 1

        if datos[0][g][2] == 'rojo':
            fr_rojo = fr_rojo + 1
        else:
            fr_negro = fr_negro + 1

        if datos[0][g][3] == 'd-1':
            fr_d1 = fr_d1 + 1
        elif datos[0][g][3] == 'd-2':
            fr_d2 = fr_d2 + 1
        else:
            fr_d3 = fr_d3 + 1
        
        fr_porvuelta.append([fr_par, fr_impar, fr_negro, fr_rojo, fr_m1, fr_m2, fr_d1, fr_d2, fr_d3])

    fr_listado = [fr_par, fr_impar, fr_negro, fr_rojo, fr_m1, fr_m2, fr_d1, fr_d2, fr_d3]
    

    df = pd.DataFrame(fr_porvuelta,
        columns=['frec par','frec impar','frec negro','frec rojo','frec m1','frec m2','frec d1','frec d2','frec d3']
    )
    print(df)
    print('frecuencias x v ', fr_porvuelta )

def main():
    resultados = []
    aux_ganadores= []
    colores = ['gold', 'darkblue', 'darkorange', 'forestgreen', 'darkorchid', 'violet', 'dark']
    r = Ruleta()
    # Instancias de Jugador (Primer parametro) => Nombre
    # Instancias de Jugador (Segundo parametro) => 0 para capital limitado 1 para ilimitado
    # Instancias de Jugador (Tercer parametro) => Metodologia de apuesta (1)- Martingala // (2)-Dalambert
    # instancias de jugador (Cuarto parametro) => A que apuesta  [par, impar, m-1 (primera mitad), m-2 (segunda mitad),
    # d-1 (primera docena), d-2 (segunda docena), d-3 (tercera docena),
    # c-1 (primer columna), c-2 (segunda columna), c-3 (tercer columna)] 
    j1 = Jugador('juan', 0, 1, 'par')
    j2 = Jugador('Andy', 0, 2, 'm-1')
    j3 = Jugador('Gonzalo', 0, 1, 'rojo')
    j4 = Jugador('Martin', 0, 2, 'c-1')

    jugadores = [j1, j2, j3, j4]

    for n in range(10):
        apuestas = []
        for j in jugadores:
            apuestas.append(j.defineJuagda())
        r.tomarApuestas(apuestas)
        r.jugar(n)
        for j in jugadores:
            j.tomarGanancia(r.pagar())
    for j in jugadores:
        resultados.append(j.devolverResultados())

    aux_ganadores = r.devolverGanadores()
    #print(aux_ganadores)
    armadataFrame(aux_ganadores)
    ######################################################################################3
    my_dpi=96
    plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)

    plt.subplot(2, 2, 1)
    aux2 = 0
    for r in jugadores:
        aux = r.devolverResultados()
        print(aux) #nuevo
        plt.plot(aux[2], aux[0], label=r.sayName(), color=colores[aux2])
        aux2 += 1
    plt.grid(True)
    plt.xlabel('n (numero de tiradas)')
    plt.ylabel('Apuestas')
    plt.legend(loc="upper left")
    plt.title('Apuestas')

    plt.subplot(2, 2, 2)
    plt.tight_layout()
    aux2 = 0
    for r in jugadores:
        aux = r.devolverResultados()
        plt.plot(aux[2], aux[1], label=r.sayName(), color=colores[aux2])
        aux2 += 1
    plt.grid(True)
    plt.xlabel('n (numero de tiradas)')
    plt.ylabel('Ganancias')
    plt.legend(loc="upper left")
    plt.title('Ganancias (no acumulativas)')

    plt.subplot(2, 2, 3)
    aux2 = 0
    for r in jugadores:
        aux = r.devolverResultados()
        if len(aux) > 4:
            plt.plot(aux[2], aux[4], label=r.sayName(), color=colores[aux2])
            aux2 += 1
        else:
            pass
    plt.grid(True)
    plt.xlabel('n (numero de tiradas)')
    y = j1.devolverResultados()
    plt.axhline(y[4][0], color='r', linestyle='-')
    plt.ylabel('CAPITAL')
    plt.legend(loc="upper left")
    plt.title('Evolucion de Capital')

    plt.subplot(2, 2, 4)
    nombres = []
    ganados = []
    for r in jugadores:
        aux = r.devolverResultados()
        nombres.append(r.sayNombre())
        ganados.append(aux[3][0])
    y_pos = np.arange(len(nombres))
    plt.bar(y_pos, ganados, align='center', alpha=0.5)
    plt.title('Ganados Por Jugador')
    plt.xticks(y_pos, nombres)

    plt.tight_layout()
    x = randint(10000, 99999)
    nombre = 'figura_TP_1_2_' + str(x) + '.png'
    plt.savefig(nombre, dpi=my_dpi)

    plt.show()

    


main()
