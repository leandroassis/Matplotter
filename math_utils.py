from sympy import *
import numpy as np
import pandas as pd

x = symbols('x')
logs = open('logsdosistema.txt','a')

def minimosquadrados(x,y):
    ab = np.linalg.inv(x.transpose().dot(x)).dot(x.transpose()).dot(y)
    return ab

def calculapontos(fx):
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
        #o objetivo dessa parte é descobrir os valores em que fx não é continua para calcular as assintotas verticais

        #calculo da primeria derivada e pontos criticos
        derv1 = factor(diff(fx,x)) 
        ncriticos = solve(derv1,x)
        xmaximoglobal = 0
        xminimoglobal = 0
        for num in ncriticos:
            try:
                y = fx.subs(x,num)
                #print(num)
                #print(y)
                if y > xmaximoglobal:
                    xmaximoglobal = num
                elif y < xminimoglobal:
                    xminimoglobal = num
                else:
                    continue
            except TypeError:
                continue
    except:
        return False
    else:
        saida = []
        saida = saida + [assintvert,xmaximoglobal, xminimoglobal]
        return saida


def ajustegrafico(pontos,opcao):
    try:
        x = []
        y = []
        x1 = []
        y1 = []
        if opcao == 1:
            for parord in pontos:
                x.append([parord[0],1])
                y.append([parord[1]])
                x1.append(parord[0])
                y1.append(parord[1])
        elif opcao == 2:
            for parord in pontos:
                x.append([parord[0]**2, parord[0],1])
                y.append([parord[1]])
                x1.append(parord[0])
                y1.append(parord[1])
        xDados = np.array(x)
        yDados = np.array(y)
        coef = minimosquadrados(xDados,yDados)
        return coef,x1,y1
    except:
        return Exception

def lerColunas(nomedoarquivo,colx,coly,ajuste):
    if '.csv' in nomedoarquivo: 
        arq = pd.read_csv(nomedoarquivo)
    else:
        arq = pd.read_excel(nomedoarquivo)
    
    yDados = arq[coly].fillna(arq[coly].mean())
    xDados = arq[colx].fillna(arq[colx].mean())
    x = []
    y = []

    for item in xDados:
        if type(item) not in [int,float]:
                continue
        else:
            x.append(item)
    for item in yDados:
        if type(item) not in [int,float]:
            continue
        else:
            y.append(item)
    xreturn = []
    if ajuste == 1:
        for dado in x:
            xreturn.append([dado,1])
    elif ajuste == 2:
        for dado in x:
            xreturn.append([dado**2,dado,1])
    else:
        return Exception
    
    xD = np.array(xreturn)
    yD = np.array(y)

    return minimosquadrados(xD,yD),x,y
    

def somafatores(lista):
    somatorio = 0
    for item in lista:
        item = sympify(item)
        somatorio = somatorio+item
    return somatorio

def calcularArea(lista,lim1,lim2):
    valores = []
    fx = sympify(lista[0])
    gx = sympify(lista[1])
    valor1  = solve(Eq(fx,gx),x)
    valor = []
    #print(valor)

    for item in valor1:
        item = str(item)
        if '*I' not in item:
            valor.append(sympify(item))
        else:
            continue

    if lim1 == None and lim2 != None:
        lim1 = valor[0]
        if lim1 > lim2:
            lim1,lim2 = lim2,lim1
        area = abs(integrate(fx-gx,(x,lim1,lim2)))
        return area
    elif lim2 == None and lim1 != None:
        lim2 = valor[len(valor)-1]
        if lim1 > lim2:
            lim1,lim2 = lim2, lim1
        area = abs(integrate(fx-gx,(x,lim1,lim2)))
        return area
    elif (lim2 and lim1) == None:    
        if len(valor) not in [0,1]:            
            for limite in range(len(valor)-1):
                try:
                    area = integrate(fx-gx,(x,valor[limite],valor[limite+1]))
                    area = abs(area)
                    valores.append(area)
                except:
                    continue
            resp = somafatores(valores)
            return resp
        elif len(valor) == 1:
            area = abs(integrate(fx-gx,(x,0,valor[0])))
            return area
    else:
        valor.append(lim1)
        valor.append(lim2)
        valor.sort()
        for limite in range(len(valor)-1):
                try:
                    area = integrate(fx-gx,(x,valor[limite],valor[limite+1]))
                    area = abs(area)
                    valores.append(area)
                except:
                    continue
        return somafatores(valores)



def calcularVolumeDisco(lista,lim1,lim2):
    valores = []
    valores2 = []
    fx = sympify(lista[0])
    gx = sympify(lista[1])
    hx = sympify(lista[2])
    valor1 = solve(Eq(fx,gx),x)
    valor = []
 
    for item in valor1:
        item = str(item)
        if '*I' not in item:
            valor.append(sympify(item))
        else:
            continue

    if lim1 == None and lim2 != None:
        lim1 = valor[0]
        if lim1 > lim2:
            lim1,lim2 = lim2,lim1
        if hx != 0:
            area1 = abs(integrate(pi*(hx-fx)**2,(x,lim1,lim2)))
            valores.append(area1)
            area2 = abs(integrate(pi*(hx-gx)**2,(x,lim1,lim2)))
            valores2.append(area2)
        else:
            area1 = abs(integrate(pi*(fx)**2,(x,lim1,lim2)))
            valores.append(area1)
            area2 = abs(integrate(pi*(gx)**2,(x,lim1,lim2)))
            valores2.append(area2)
        return abs(somafatores(valores)-somafatores(valores2))
    
    elif lim2 == None and lim1 != None:
        lim2 = valor[len(valor)-1]
        if lim1 > lim2:
            lim1,lim2 = lim2, lim1
        if hx != 0:
            area1 = abs(integrate(pi*(hx-fx)**2,(x,lim1,lim2)))
            valores.append(area1)
            area2 = abs(integrate(pi*(hx-gx)**2,(x,lim1,lim2)))
            valores2.append(area2)
        else:
            area1 = abs(integrate(pi*(fx)**2,(x,lim1,lim2)))
            valores.append(area1)
            area2 = abs(integrate(pi*(gx)**2,(x,lim1,lim2)))
            valores2.append(area2)
        return abs(somafatores(valores)-somafatores(valores2))
    
    elif (lim2 and lim1) == None:    
        if len(valor) not in [0,1]:            
            for limite in range(len(valor)-1):
                try:
                    if hx != 0:
                        area1 = abs(integrate(pi*(hx-fx)**2,(x,valor[limite],valor[limite+1])))
                        valores.append(area1)
                        area2 = abs(integrate(pi*(hx-gx)**2,(x,valor[limite],valor[limite+1])))
                        valores2.append(area2)
                    else:
                        area1 = abs(integrate(pi*(fx)**2,(x,valor[limite],valor[limite+1])))
                        valores.append(area1)
                        area2 = abs(integrate(pi*(gx)**2,(x,valor[limite],valor[limite+1])))
                        valores2.append(area2)
                except:
                    continue
            resp1 = somafatores(valores)
            resp2 = somafatores(valores2)
            return abs(resp1-resp2)
        elif len(valor) == 1:
            if hx != 0:
                area1 = abs(integrate(pi*(hx-fx)**2,(x,0,valor[0])))
                valores.append(area1)
                area2 = abs(integrate(pi*(hx-gx)**2,(x,0,valor[0])))
                valores2.append(area2)
            else:
                area1 = abs(integrate(pi*(hx-fx)**2,(x,0,valor[0])))
                valores.append(area1)
                area2 = abs(integrate(pi*(hx-gx)**2,(x,0,valor[0])))
                valores2.append(area2)    
            return abs(somafatores(valores)-somafatores(valores2))
        elif len(valor) == 0:
            return Exception
    else:
        valor.append(lim1)
        valor.append(lim2)
        valor.sort()
        for limite in range(len(valor)-1):
            try:
                if hx != 0:
                    area1 = abs(integrate(pi*(hx-fx)**2,(x,valor[limite],valor[limite+1])))
                    valores.append(area1)
                    area2 = abs(integrate(pi*(hx-gx)**2,(x,valor[limite],valor[limite+1])))
                    valores2.append(area2)
                else:
                    area1 = abs(integrate(pi*(hx-fx)**2,(x,valor[limite],valor[limite+1])))
                    valores.append(area1)
                    area2 = abs(integrate(pi*(hx-gx)**2,(x,valor[limite],valor[limite+1])))
                    valores2.append(area2)
            except:
                continue
        resp1 = somafatores(valores)
        resp2 = somafatores(valores2)
        return abs(resp1-resp2)
    

def calcularVolumeCilindro(lista,lim1,lim2):
    valores = []
    fx = sympify(lista[0])
    gx = sympify(lista[1])
    valor1 = solve(Eq(fx,gx),x)
    valor = []

    for item in valor1:
        item = str(item)
        if '*I' not in item:
            valor.append(sympify(item))
        else:
            continue
    
    if lim1 == None and lim2 != None:
        lim1 = valor[0]
        if lim1 > lim2:
            lim1,lim2 = lim2,lim1
            area1 = integrate(2*pi*x*(fx-gx),(x,lim1,lim2))
        return abs(area1)
    
    elif lim2 == None and lim1 != None:
        lim2 = valor[len(valor)-1]
        if lim1 > lim2:
            lim1,lim2 = lim2, lim1
            area1 = integrate(2*pi*x*(fx-gx),(x,lim1,lim2))
        return abs(area1)
    
    elif (lim2 and lim1) == None:    
        
        if len(valor) not in [0,1]:            
            for limite in range(len(valor)-1):
                try:
                    area1 = integrate(2*pi*x*(fx-gx),(x,valor[limite],valor[limite+1]))
                    valores.append(area1)
                except:
                    continue
            resp1 = somafatores(valores)
            return abs(resp1)
        
        elif len(valor) == 1:
            area1 = abs(integrate(2*pi*x*(gx-fx)**2,(x,0,valor[0])))
            return abs(area1)
    
    else:
        valor.append(lim1)
        valor.append(lim2)
        valor.sort()
        for limite in range(len(valor)-1):
            try:
                area1 = integrate(2*pi*x*(fx-gx),(x,valor[limite],valor[limite+1]))
                valores.append(area1)
            except:
                continue
        resp1 = somafatores(valores)
        return abs(resp1)
