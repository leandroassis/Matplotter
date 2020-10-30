from sympy import *
import numpy as np

x = symbols('x')
def drawcurve(fx):
    try:
        #Domínio de f(x)
        funcinversa = fx**-1
        numforadominio = solve(funcinversa,x)
        assintvert = []
        for n in numforadominio:
            n = str(n)
            try:
                if 'I' in n == True:
                    continue
                else:
                    n = sympify(n)
                    assintvert = assintvert + [n]
            except IndexError:
                continue
        #print(numforadominio)
        #print(assintvert)
        #o objetivo dessa parte é descobrir os valores em que fx não é continua para calcular as assintotas verticais

        #calculo da primeria derivada e pontos criticos
        derv1 = factor(diff(fx,x)) 
        ncriticos = solve(derv1,x)
        #print(ncriticos)
        xmaximoglobal = 0
        xminimoglobal = 0
        for num in ncriticos:
            try:
                y = fx.subs(x,num)
                print(num)
                print(y)
                if y > xmaximoglobal:
                    xmaximoglobal = num
                elif y < xminimoglobal:
                    xminimoglobal = num
                else:
                    continue
            except TypeError:
                continue
        #print(xmaximoglobal)
        #print(xminimoglobal)


        #print(derv1)
        #print(ncriticos)
    except:
        return False
    else:
        saida = []
        saida = saida + [assintvert,xmaximoglobal, xminimoglobal]
        #print(saida)
        return saida


#print(drawcurve(sin(x)))
