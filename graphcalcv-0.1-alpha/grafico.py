import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import random as rd

x = symbols('x')

def calcy(valoresdex, func):
    x = symbols('x')   
    ydados = []
    for b in valoresdex:
        y1 = func.subs(x,b)
        ydados.append(y1)
        #print('cheguei aq mano')
        #print(y1)
    return ydados

def plotar(pontos,funcao,cont=0):
    funcao = sympify(funcao)        
    if True:
        numforadominio = pontos[0]
        xmaximoglobal = pontos[1]
        xminimoglobal = pontos[2]
        #print(numforadominio)
        #print(xmaximoglobal)
        #print(xminimoglobal)


        #calcula os limites esboçados no gráfico:
        if xmaximoglobal < 0:
            xmaximoglobal = xmaximoglobal*-1
        if xminimoglobal < 0:
            xminimoglobal = xminimoglobal*-1
        final = 3*(xmaximoglobal+xminimoglobal)//2
        inicial = -3*(xmaximoglobal+xminimoglobal)//2    
        if final == 0 and inicial == 0:
            final = rd.randint(0,30)
            inicial = -1*final 
        #print(final)
        #print(inicial)

        #anota os valores das assintotas verticais
        assintvert = []
        for ponto in numforadominio:
            pontopdireita = 1.02*ponto
            pontopesquerda = 0.998*ponto
            assintvert = assintvert + [pontopesquerda,pontopdireita]
        #print(assintvert)
        
        #ordena os valores das assintotas atraves de um bubble sort
        aux = 0
        while aux <= len(assintvert):
            i = 0
            i1 = 1
            while i1 < len(assintvert)-aux:
                if assintvert[i] > assintvert[i1]:
                    assintvert[i],assintvert[i1] = assintvert[i1], assintvert[i]
                else:
                    i = i+1
                    i1 = i1+1
                    continue
                i = i+1
                i1 = i1+1
            aux = aux+1
        
        #gerando o gráfico
        if len(assintvert) > 0:
            liber = 0
            for valor in range(len(assintvert)):
                if len(assintvert) > 2:
                    if valor%2==0:
                        xdados = np.arange(inicial,assintvert[valor],0.01)
                        inicial = assintvert[valor]
                    elif valor%2==1:
                        inicial = assintvert[valor]
                        xdados = np.arange(inicial,assintvert[valor+1],0.01)
                        inicial = assintvert[valor+2]
                    if valor == len(assintvert) - 2:
                        xdados = np.arange(assintvert[valor+1],final,0.01)
                        liber = 1
                    else:
                        pass
                    plt.plot(xdados,calcy(xdados,funcao))
                    if liber == 1:
                        break
                    else:
                        continue
                elif len(assintvert) == 2:
                    numero = 0
                    if valor == 0:
                        xdados = np.arange(inicial,assintvert[valor],0.01)
                    elif valor == 1:
                        xdados = np.arange(assintvert[1],final,0.01)
                    plt.plot(xdados,calcy(xdados,funcao))
        else:
            xdados = np.arange(inicial,final,0.01)
            plt.plot(xdados, calcy(xdados,funcao))

    '''
    else:
        x = symbols('x')
        #print(cont)
        xdados = np.arange(0,180,0.1)
        plt.plot(xdados,calcy(xdados,funcao))
    
    
    #configurações do gráfico
    '''



    #salva e apresenta o gráfico
    plt.show()
    plt.savefig('figura%d'%cont)
    plt.close()
    cont = cont+1
    return None
    

#plotar([[-1,0,1],0,2],'x**32')
#plotar([[1],-90,90],'sin(x)/(x-1)')
#plotar('functrigonometrica','sin(x)')
#plotar([[],0,0],2**x)
