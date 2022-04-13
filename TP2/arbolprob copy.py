import pandas as pd
import numpy as np

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
    
    df = pd.DataFrame(resultados_posibles[len(resultados_posibles)-1],
        columns=['cadena de resultado','probabilidad','nro de tirada']
    )

    df2 = pd.DataFrame(df['probabilidad'].value_counts())

                
    df2['f_r']= df2.index * df2['probabilidad']

    
    df2.loc['Total'] = df2['f_r'].sum()

    print(df2)
    print(df)

    #df.merge(df2, on=['index', 'V2'], how='outer').dropna()

main()
