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
        #print(y1)
    return ydados

def plotar(pontos,funcao):
    cont = rd.randint(0,99999)
    try:
        funcao = sympify(funcao)        
        numforadominio = pontos[0]
        xmaximoglobal = pontos[1]
        xminimoglobal = pontos[2]
        #print(numforadominio)
        #print(xmaximoglobal)
        #print(xminimoglobal)
        
        #calcula os limites esboçados no gráfico:
        xmaximoglobal = str(xmaximoglobal)
        xminimoglobal = str(xminimoglobal)
        if 'I' in xmaximoglobal:
            xmaximoglobal = 0
        if 'I' in xminimoglobal:
            xminimoglobal = 0
        xminimoglobal = abs(sympify(xminimoglobal))
        xmaximoglobal = abs(sympify(xmaximoglobal))
        #print(xmaximoglobal)
        #print(xminimoglobal)
        final = 5*(xmaximoglobal+xminimoglobal)
        inicial = -1*final    
        if final == 0 and inicial == 0:
            final = rd.randint(0,30)
            inicial = -1*final 
        #print(final)
        #print(inicial)
            
        #anota os valores das assintotas verticais
        assintvert = []
        for ponto in numforadominio:
            if ponto == 0:
                pontopdireita == 1.15*0.3
                pontopesquerda == 0.85*0.3
            else:
                pontopdireita = 1.15*ponto
                pontopesquerda = 0.85*ponto
            assintvert = assintvert + [pontopesquerda,pontopdireita]
        #print(assintvert)
        
        #ordena os valores das assintotas
        assintvert.sort()

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
                    plt.plot(xdados,calcy(xdados,funcao),color = 'r')
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
                    plt.plot(xdados,calcy(xdados,funcao),color = 'r')
        else:
            xdados = np.arange(inicial,final,0.01)
            plt.plot(xdados, calcy(xdados,funcao))
            
        #configurações do gráfico
        #plt.axes().spines['bottom'].set_position(('data',0))
        plt.axes().spines['left'].set_position(('data',0))
        #plt.axvline(ymin=0, color= 'k')
        plt.axvline(plt.xlim()[0], color= 'k')
        plt.grid()
        
        plt.title(str(funcao))
        #salva e apresenta o gráfico
        plt.show()
        plt.savefig('grafico%d'%cont)
        plt.close()
    except:
        print('Não conseguimos resovler esse problema ainda...')
        return False

def esbocoajustecurvas(coef,xplot,yplot,ajuste):
    saiday = []
    contador = rd.randint(0,100)

    if ajuste == 1:
        for valor in xplot:
            y = coef[0]*valor + coef[1]
            saiday.append(y)
        plt.plot(xplot,saiday)
        plt.legend('Curva Ajustada')
        plt.title('Ajuste Linear')
    
    elif ajuste == 2:
        xplot2 = xplot
        xplot2.sort()
        xparaplotar = np.arange(xplot2[0],xplot2[len(xplot2)-1],0.01)
        for valor in xparaplotar:
            y = coef[0]*valor**2 + coef[1]*valor + coef[2]
            saiday.append(y)
        plt.plot(xparaplotar,saiday)
        plt.legend('Curva Ajustada')
        plt.title('Ajuste Quadrático')
    
    # configurando o grafico
    plt.scatter(xplot,yplot,color = 'g')
    plt.legend('Pontos mensurados')
    
    xplot.sort()
    #plt.xlim(xplot[0],xplot[len(xplot)-1])

    plt.show()
    plt.savefig('ajuste%d.png'%contador)
    plt.close()
