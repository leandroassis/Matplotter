from sympy import *
import os
from math_utils import *
from plot_utils import *
init_printing(use_unicode=True)

def main():
    x = symbols('x')
    os.system('clear')
    logs = open('logsdosistema.txt', 'a')
    logs.write('\n\n\n')
    logs.write('-----------------\n')
    logs.write('Programa Iniciado\n')
    while True:
        logs.write('Menu Principal \n')
        print('Bem Vindo ao GraphCalcI')
        print('\nMENU INICIAL:\n')
        print('1 - Esboçar gráfico de uma função inserida.')
        print('- Ajuste de funções lineares/não lineares.')
        print('    2 - Utilizar dados inseridos manualmente.')
        print('    3 - Utilizar dados retirado de arquivo.')
        print('4 - Calculadora Áreas e Volumes.') 
        print('5 - Logs do Sistema.')
        print('6 - Ajuda.')
        print('7 - Sair.\n\n')
        print('\nDesenvolvido por Leandro Assis dos Santos')
        try:
            choice = input('\nEscolha uma das opções: ')       
            choice = int(choice)
            if choice not in [1,2,3,4,5,6,7]:
                raise ValueError
        except KeyboardInterrupt:
            print('\nEncerrando o programa...\n\n')
            break
        except ValueError:
            os.system('clear')
            print('\nErro! O valor inserido não é válido.\n')
        else:
            os.system('clear')

            if choice == 1:
                logs.write('Opção 1 - Esboço de curvas escolhida.\n')
                while True:
                    try:
                        os.system('clear')
                        func = input('Insira a função que deseja esboçar: (não digite nada para sair)\n')
                        logs.write('Função Inserida: %s\n' %func)
                        if func in ['',' ']:
                            raise KeyboardInterrupt
                        else:
                            func = sympify(func)
                    except KeyboardInterrupt:
                        os.system('clear')
                        logs.write('Interrupção do usuário \n')
                        print('\nRetornando ao Menu Principal...\n') 
                        break
                    except:
                        print('\nErro! A equação inserido não é válida, verifique antes de inserir novamente\n')
                        logs.write('Erro encontrado, valor anterior descartado. Insira novamente.\n')
                    else:
                        os.system('clear')          
                        logs.write('Chamada de função para calcular os pontos da função:' +str(func)+'.\n')                      
                        pontos = calculapontos(func)
                        if pontos == False:
                            os.system('clear')
                            print('Não somos capaz de solucionar essa equação ainda...\n\n')
                            logs.write('Problema Não Suportado no momento...\n')
                            break
                        else:
                            logs.write('Chamada da função para gerar o gráfico.\n')
                            plotagem = plotar(pontos,func)
                        if plotagem == False:
                            break
                        logs.write('Ciclo encerrado - Retornando ao Menu.\n')
            elif choice == 2 or choice == 3:
                logs.write('Opção de Ajuste de Curvas Escolhida.\n')
                while True:
                    print('Qual o ajuste da função?')
                    print('1 - Linear')
                    print('2 - Quadrática')
                    try:
                        tipocurva = input('Insira a opção:\n')
                        tipocurva = int(tipocurva)
                        logs.write('Escolha do tipo de ajuste linear: %d escolhido.\n'%tipocurva)
                        if tipocurva < 1 or tipocurva > 2:
                            raise ValueError
                    except ValueError:
                        os.system('clear')
                        print('\n\nErro! O valor inserido não é válido. Verifique antes de inserir novamente\n\n')
                    except KeyboardInterrupt:
                        print('\nEncerrando o programa.')
                        choice = 0
                        break
                    else:
                        break
            if choice == 2:
                parord = []
                while True:
                    logs.write('Usuário inserindo valores para os pares ordenados\n')
                    try:
                        x = input('\nInsira o valor de x. Digite exit para sair e não digite nada para gerar o gráfico.\n')
                        y = input('\nInsira o valor de y. Digite exit para sair e não digite nada para gerar o gráfico.\n')
                        if (x == '') or (y == ''):
                            os.system('clear')
                            sair = False
                            break
                        elif (x.lower()=='exit') or (y.lower()=='exit'):
                            os.system('clear')
                            print('Retornando ao menu principal...\n\n')
                            sair = True
                            break
                        y = int(y)
                        x = int(x)
                    except KeyboardInterrupt:
                        print('\nRetornando...')
                        break
                    except ValueError:
                        try:
                            y = float(y)
                            x = float(x)
                        except ValueError:
                            print('Você digitou valores inválidos que serão descartados.')
                            continue
                        else:
                            parord = parord + [[x,y]]
                    else:
                        parord = parord + [[x,y]]
                        os.system('clear')
                        logs.write('Foram inseridos os seguintes pares ordenados: %s.\n' %str(parord))
                        print('\nOs pares ordenados são %s'%str(parord))
                if sair != True:
                    try:
                        logs.write('Chamada das funções para calcular os coeficientes e gerar os gráficos.\n')
                        coeficiente,xpontos,ypontos = ajustegrafico(parord,tipocurva)
                        esbocoajustecurvas(coeficiente,xpontos,ypontos,tipocurva)
                        print('Os valores dos coeficientes são : %s'%coeficiente)
                    except:
                        print('Ocorreu um erro, verifique as entradas!\n')
                        logs.write('Erro detectado.\n')
            if choice == 3:
                os.system('clear')
                logs.write('Ajuste de dados em arquivo escolhido.\n')
                while True:
                    try:
                        arqname = input('\nInsira o nome do arquivo (com extensão .csv ou .xlsx-e similares-) com os dados.\n')
                        xDados = input('Digite o nome da coluna com os dados do eixo X:\n')
                        yDados = input('Digite o nome da coluna com os dados do eixo Y:\n')
                        logs.write('Ajute de %s em função de %s do arquivo %s.\n'%(xDados,yDados,arqname))
                    except KeyboardInterrupt:
                        os.system('clear')
                        print('\nEncerrando...')
                        break
                    try:
                        coef,x,y = lerColunas(arqname,xDados,yDados,tipocurva)
                    except FileNotFoundError:
                        os.system('clear')
                        print('Não foi possível encontrar o arquivo. Verifique se está passando o caminho/nome correto.')
                    except:
                        os.system('clear')
                        print('Ocorreu um erro, verifique os dados das colunas passadas.')
                        logs.write('Erro ao executar ajuste.\n')
                    else:
                        esbocoajustecurvas(coef,x,y,tipocurva)
                        logs.write('O gráfico foi gerado com coeficiente %s.\n'%str(coef))
                        os.system('clear')
                        print('Os coeficientes são %s'%str(coef))
                        break
                    
            
            if choice == 4:
                logs.write('Opção 4 - Calculadora de áreas e volumes escolhida.\n')
                os.system('clear')
                curvas = []
                while True:
                    try:
                        print('Calculadora de Volumes e Áreas de curvas.')
                        print('\n1 - Cálculo de Áreas.')
                        print('2 - Cálculo de Volumes (Método dos discos - rotação em torno de eixo paralelo ao eixo x).')
                        print('3 - Cálculo de Volumes. (Método das cascas cilíndricas - rotação em torno de eixo paralelo ao eixo y)')
                        print('Não digite nada para sair.')
                        op = input('Escolha uma opção: ')
                        logs.write('O usuário escolheu a opção %s.\n' %op)
                    except KeyboardInterrupt:
                        os.system('clear')
                        print('Encerrando...')
                        conti = False
                        logs.write('Operação Encerrada pelo usuário.\n')
                        break
                    else:
                        if op in ['',' ','  ']:
                            os.system('clear')
                            print('Retornando...')
                            break
                        else:
                            try:
                                op = int(op)
                            except:
                                os.system('clear')
                                print('Você inseriu um valor inválido. Verifique e tente novamente.\n')
                    if op == 1:
                        aux = 1
                        conti = True
                        while aux <= 2:
                            os.system('clear')
                            try:
                                equacao = input('Digite a equação da curva %d:'%aux)
                                logs.write('Equação para a curva %d: %s.\n' %(aux,equacao))
                                equacao = sympify(equacao)
                            except KeyboardInterrupt:
                                os.system('clear')
                                print('Encerrando...')
                                conti = False
                                break
                            except:
                                equacao = 0
                            curvas.append(equacao)
                            aux=aux+1
                        if conti == True:
                            limite1 = input('Insira o limite inferior de integração (Não insira nada se quiser usar um ponto de encontro das curvas):')
                            limite2 = input('Insira o limite superior de integração (Não insira nada se quiser usar um ponto de encontro das curvas):')
                            logs.write('Limites para a integração inseridos %s,%s.\n'%(limite1,limite2))
                            try:
                                limite1 = sympify(limite1)
                                limite2 = sympify(limite2)
                            except:
                                limite1 = None
                                limite2 = None
                            try:
                                logs.write('Chamada da função para calcular áreas.\n')
                                Area = calcularArea(curvas,limite1,limite2)
                            except:
                                os.system('clear')
                                print('Ocorreu um erro durante a resolução do problema inserido, verifique e tente novamente.')
                            else:
                                os.system('clear')
                                print('A área da região é: ' + str(Area) + '.\n')
                                logs.write('A área é: %s'%str(Area))
                                curvas = []
                                break
                    elif op == 2:
                        os.system('clear')
                        logs.write('Iniciado cálculo de volume em eixo paralelo ao eixo x.\n')
                        print('Não se esqueça de inserir 3 equações, sendo as duas primeiras em função de x e a terceira a curva que servirá como eixo de giro.')
                        aux = 0
                        conti = True
                        while aux <3:
                            aux = aux+1
                            try:
                                logs.write('Usuário delimitando região para o cálculo do volume.\n')
                                retas = input('Insira a reta %d que delimita a região. (Digite 0 para pular):'%aux)
                            except KeyboardInterrupt:
                                os.system('clear')
                                print('Encerrando...')
                                conti = False
                                break
                            if retas in ['',' ']:
                                os.system('clear')
                                print('Retornando...')
                                conti = False
                                break
                            else:
                                try:
                                    retas = sympify(retas)
                                except:
                                    retas = 0
                                curvas.append(retas)
                        try:
                            logs.write('A região foi delimitada entre y = %s e y = %s girando em torno de y = %s.\n'%(str(curvas[0]),str(curvas[1]),str(curvas[2])))
                        except:
                            pass
                        if conti == True:
                            os.system('clear')
                            limite1 = input('Insira o limite inferior de integração (Não insira nada se quiser usar um ponto de encontro das curvas):')
                            limite2 = input('Insira o limite superior de integração (Não insira nada se quiser usar um ponto de encontro das curvas):')
                            logs.write('Limites de integração selecionados como a = %s e b = %s.\n'%(limite1,limite2))
                            try:
                                limite1 = sympify(limite1)
                                limite2 = sympify(limite2)
                            except:
                                limite1 = None
                                limite2 = None
                            try:
                                logs.write('Chamada da função para calcular volume pelo método dos discos.\n')
                                Volume = calcularVolumeDisco(curvas,limite1,limite2)
                                print(Volume)
                            except:
                                os.system('clear')
                                print('Ocorreu um erro. Verifique as entradas antes de tentar novamente')
                            else:
                                os.system('clear')
                                print('O volume do sólido formado pela rotação é: ' +str(Volume)+'.\n')
                                logs.write('O resultado é %s.\n'%str(Volume))
                                break
                    elif op == 3:
                        os.system('clear')
                        logs.write('Iniciando cálculo de volume em eixo paralelo ao eixo y.\n')
                        aux = 0
                        conti = True
                        while aux <2:
                            aux = aux+1
                            try:
                                logs.write('Usuário delimitando a região da área.\n')
                                retas = input('Insira a reta %d que delimita a região. (Digite 0 para pular):'%aux)
                            except KeyboardInterrupt:
                                os.system('clear')
                                print('Encerrando...')
                                conti = False
                                break
                            if retas in ['',' ']:
                                os.system('clear')
                                print('Retornando...')
                                conti = False
                                break
                            else:
                                try:
                                    retas = sympify(retas)
                                except:
                                    retas = 0
                                curvas.append(retas)
                        logs.write('A região foi delimitada entre y=%s e y=%s, em torno de x = 0.\n'%(str(curvas[0]),str(curvas[1])))
                        if conti == True:
                            os.system('clear')
                            limite1 = input('Insira o limite inferior de integração (Não insira nada se quiser usar um ponto de encontro das curvas):')
                            limite2 = input('Insira o limite superior de integração (Não insira nada se quiser usar um ponto de encontro das curvas):')
                            logs.write('Escolha dos limites de integração como a = %s e b = %s.\n'%(str(limite1),str(limite2)))
                            try:
                                limite1 = sympify(limite1)
                                limite2 = sympify(limite2)
                            except:
                                limite1 = None
                                limite2 = None
                            try:
                                logs.write('Chamada da função para calcular o volume no método das cascas cilíndricas. \n')
                                Volume = calcularVolumeCilindro(curvas,limite1,limite2)
                            except:
                                os.system('clear')
                                print('Ocorreu um erro. Verifique as entradas antes de tentar novamente')
                            else:
                                os.system('clear')
                                print('O volume do sólido formado pela rotação é: ' +str(Volume)+'.\n')
                                logs.write('O resultado é: %s.\n' %str(Volume))
                                break
                    else:
                        os.system('clear')
                        print('Você inseriu um valor inválido, verifique antes de tentar novamente.')

                    
                        
            elif choice == 5:
                logs.write('Abertura dos Registros.\n')
                systemlog = open('logsdosistema.txt','r')
                os.system('clear')
                print(systemlog.read())
                for linha in systemlog:
                    linhas = systemlog.read()
                    print(linhas)
                systemlog.close()
            elif choice == 6:
                logs.write('Leitura do Manual de Instruções.\n')
                ajuda = open('ajuda.txt','r')
                os.system('clear')
                print(ajuda.read())
                for linha in ajuda:
                    linhas = ajuda.read()
                    print(linhas)
                while True:
                    sair = input('Aperte enter para sair ')
                    if sair == '':
                        os.system('clear')
                        break
                    else:
                        continue
                ajuda.close()
            elif choice == 7:
                logs.write('Programa Encerrado.\n')
                logs.write('-------------------\n')
                os.system('clear')
                print('\nObrigado por utilizar o GraphCalcI!!!')
                break
            else:
                continue
    logs.close()

if __name__ == '__main__':
    main()

