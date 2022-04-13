import pandas as pd

def main():
    n = 5 #numero de ciclos

    resultados_posibles = []
    arr_aux =[]
    arr_aux2 =[]

    p_ganar = 18/37 #probabilidad de ganar
    p_perder = 19/37 #probabilidad de perder que es la probabilidad de que salga lo contrario a lo apostado + 0

    for i in range(n):
        if len(resultados_posibles) == 0:
            resultados_posibles.append([['g', p_ganar, i],['p', p_perder, i]])
        else:
            for r in resultados_posibles[len(resultados_posibles)-1]:
                arr_aux.append([ r[0] + 'g', p_ganar*r[1], i])
                arr_aux.append([r[0] + 'p', p_perder*r[1], i])
            resultados_posibles.append(arr_aux)
            arr_aux =[]
    #print('res:', resultados_posibles)
    
    arr_aux =[]
    for r in resultados_posibles:
        for x in r:
            arr_aux.append(x)
    print(arr_aux)
    df = pd.DataFrame(arr_aux,
        columns=['cadena de resultado','probabilidad','nro de tirada']
    )


    print(df)
                


main()
