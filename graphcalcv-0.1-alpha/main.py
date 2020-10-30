#import numpy as np
#import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
from sympy import *
import os
from drawcurve import drawcurve
from grafico import plotar
init_printing(use_unicode=True)


'''
def calcfunc(funcao):
    derivada = funcao.diff(x)
    valor = solve(Eq(derivada,0),x)
    for num in valor:
'''        
'''
def resultpolin(x1,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0,grau=2):
    resultado = []
    n = grau
    # IMPLEMENTAR ALOCAÇÃO DINAMICA RECEBENDO UMA LISTA DA FUNÇÃO MINIMOSQUADRADSO E CRIANDO UMA VARIAVEL PARA CADA VALOR DE X DA LISTA
    for z in x1:
        valor = a*z**n+b*z**(n-1)+c*z**(n-2)+d*z**(n-3)+e*z**(n-4)+f*z**(n-5)+g*z**(n-6)+h*z**(n-7)+i*z**(n-8)+j*z**(n-9)+k*z**(n-10)
        resultado = resultado+[valor]
        return resultado
    #DESENVOLVER PARTE DE CALCULO DOS PARES ORDENADOS OBS: USAR SYMPY PARA PARES ORDENADOS E INFINITOS PARES ORDENADOS EM FUNÇÕES TRIGONOMETRICAS E RACIONAIS

pontos = [[-4,17],[-1,8],[0,9],[2,17]]
x1, x2,x3 = minimosQuadrados(pontos)
print(x1,x2,x3)
#DESENVOLVER PARTE DE CALCULO DOS GRAFICOS
a = np.arange(-4.0,2.01,0.01) 
plt.scatter([-4,-1,0,2],[17,8,9,17])
plt.plot(a,resultpolin(a,x1,x2,x3,grau=2))
plt.yticks(np.arange(0,20,2))
plt.savefig('asdkljsad.png')
'''

def main():
    x = symbols('x')
    os.system('clear')
    cont = 0
    while True:
        print('Bem Vindo ao GraphCalcI')
        print('\n\nMENU INICIAL:\n')
        print('1 - Esboçar gráfico de uma função inserida.')
        print('- Ajuste de funções lineares/não lineares.')
        print('    2 - Utilizar dados inseridos manualmente.')
        print('    3 - Utilizar dados retirado de arquivo.')
        print('4 - Calculadora de Cálculo I (Limites,Derivadas,Integrais).')
        print('5 - Logs do Sistema.')
        print('6 - Ajuda.')
        print('7 - Sair.\n\n')
        print('\nDesenvolvido por Leandro Assis dos Santos')
        try:
            choice = input('\nEscolha uma das opções: ')       
            choice = int(choice)
            if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7:
                raise ValueError
        except KeyboardInterrupt:
            print('\nEncerrando o programa...')
            print('')
            print('')
            break
        except ValueError:
            os.system('clear')
            print('\nErro! O valor inserido não é válido.\n')
        else:
            if choice == 1:
                continuar = False
                while True:
                    try: 
                        func = input('Insira uma função válida (consulte ajuda):\n')
                        func = sympify(func)
                    except KeyboardInterrupt:
                        print('\nEncerrando...')
                        break
                    except:
                        print('\nErro! o valor inserido não é válido, verifique antes de inserir novamente\n')
                    else:
                        os.system('clear')                                
                        pontos = drawcurve(func)
                        if pontos == False:
                            os.system('clear')
                            print('Não somos capaz de solucionar essa equação ainda...\n\n')
                            break
                        else:
                            plotar(pontos,func,cont)
                            cont = cont+1
                        '''
                        continuar = input('Deseja inserir outra função nesse gráfico? S/N')
                        if continuar.lower() == 's':
                            continuar = True                            
                            os.system('clear')
                            continue
                        if continuar.lower() == 'n':
                            print('Você escolheu encerrar')
                            break
                        else:
                            print('Não compreendi.Voltando ao menu principal...')
                            break
                        '''    
            elif choice == 2 or choice == 3:
                while True:
                    os.system('clear')
                    print('Qual o ajuste da função?')
                    print('1 - Linear')
                    print('2 - Exponencial')
                    print('3 - Geométrica')
                    print('4 - Polinomial')
                    try:
                        tipocurva = input('Insira a opção:\n')
                        tipocurva = int(tipocurva)
                        if tipocurva < 1 or tipocurva > 4:
                            raise ValueError
                    except ValueError:
                        print('\n\nErro! O valor inserido não é válido.\n\n')
                    except KeyboardInterrupt:
                        print('\nEncerrando o programa.')
                        break
                    else:
                        break
            if choice == 2:
                parord = [] #adicionar teste try
                while True:
                    xey = input('\nInsira o valor do par ordenado separando os valores por vírgula ex: x,y. Não digite nada para sair.\n')
                    if xey == '':
                        break
                    else:
                        parord = parord + [[xey]]
                        os.system('clear')
                        print(xey)
                        print(parord)
                        #adicionar valor em função para o ajuste (ajuste(parord, tipocurva))
                        #adicionar o valor retornado para a funçãp de ajuste em uma função para gerar graficos (graficos(a,b,c,tipocurva,x1,xf,y1,yf))
                        
            if choice == 3:
                while True:
                    try:
                        arqname = input('\nInsira o nome do arquivo(com extensão) com os dados.\n')
                        '''
                        arq = open(arqname)
                        except FileNotFoundError:
                        print('Arquivo não encontrado.')
                        adicionar essa parte na funcao lerarquivos
                        '''
                    except KeyboardInterrupt:
                        print('\nEncerrando...')
                        break
                    else:
                        xDados = input('Digite o nome da coluna com os dados do eixo X:\n')
                        yDados = input('Digite o nome da coluna com os dados do eixo Y:\n')
                        os.system('clear')
                        break
                        #adicionar try
                        #adicionarfunção learquivos(tipocurva,arqname,xDados,yDados)
            if choice == 4:
                while True:
                    try:
                        print('\nCalculadora de Cálculo I\n\nNão digite nada para sair\n')
                        equacao = input('Digite a equação que deseja calcular (consulte ajuda):\n')
                    except KeyboardInterrupt:
                        print('\nEncerrando...')
                        break
                    except:
                        print('Erro! O verifique o valor inserido')
                    else:                  
                        if equacao == '':
                            os.system('clear')
                            break
                        else:
                            os.system('clear')
                            equacao = sympify(equacao)
                            pprint(equacao)
                            continue
                        
            elif choice == 5:
                systemlog = open('logsdosistema.txt','r')
                #para cada função os valores dos operadores devem ser salvos nesse arquivo
                #se o sistema for reiniciado os logs devem ser apagados
                linhas = systemlog.readlines()
                os.system('clear')
                print(linhas)
                systemlog.close()
            elif choice == 6:
                ajuda = open('ajuda.txt','r')
                linhas = ajuda.readlines()
                os.system('clear')
                print(linhas)
                while True:
                    sair = input('Aperte enter para sair ')
                    if sair == '':
                        break
                    else:
                        continue
                    ajuda.close()
            elif choice == 7:
                os.system('clear')
                print('\nObrigado por utilizar o GraphCalcI!!!')
                break
            else:
                continue

main()
