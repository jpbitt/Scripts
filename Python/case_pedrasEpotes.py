import random as rd
import math as mt
import numpy as np

tabela = [] #TABELA ONDE SERÃO ARMAZENADOS OS DADOS

#---------------------------
# RECEBE AS INFORMAÇÕES DO USUÁRIO
#---------------------------
def recebe_valores():
    print("Joãozinho deseja distruibuir um numero N de pedras em um numero M de potes")
    pedra = int(input("Forneça o número de PEDRAS: "))
    pote = int(input("Forneça o número de POTES: "))
    print("------------------------------")
    print("O número de {} pedras e {} potes".format(pedra,pote))
    return pedra,pote
#---------------------------
# VALIDA AS INFORMAÇÕES DO USUARIO, DEVE ATENDER A REGRA "O NUMERO DE PEDRAS DEVE SER MAIOR QUE O NUMERO DE POTES"
#---------------------------
def valida_dados(pedra,pote):

    while True:
        print("------------------------------")
        print("VALIDANDO OS NUMEROS INSERIDOS")
        print("------------------------------")
        if pote <= 0:
            print("ERRO DE VALIDAÇÃO")
            print("O NUMERO DE POTES DEVE SER MAIOR QUE 0")
            pote = int(input("Por favor, forneça o número de POTES correto: "))
        elif pedra <= 1:
            print("ERRO DE VALIDAÇÃO")
            print("O NUMERO DE PEDRAS DEVE SER MAIOR QUE 1")
            pedra = int(input("Por favor, forneça o número de PEDRAS correto: ")) 
        elif pote >= pedra:
            print("ERRO DE VALIDAÇÃO")
            print("O NUMERO DE POTES DEVE SER MENOR QUE O NUMERO DE PEDRAS")
            pote = int(input("Por favor, forneça o número de POTES correto: ")) 
        else:   
            print("VALIDAÇÃO CONCLUIDA COM SUCESSO")
            print("------------------------------") 
            print("Joãozinho tem {} pedras e {} potes".format(pedra,pote))
            print("------------------------------")
            break
    return pedra,pote
#---------------------------
# ORGANIZA AS PEDRAS EM CADA POTE  
#---------------------------
def gera_tabela(tabela,pedra,pote):
    
    lista = list(range(1,pedra-pote+2))
    for i in range(mt.factorial(pedra)):
        linha = [] # criamos a linha
        for j in range(pote):
            valor = rd.choice(lista) # gera valor aleatorio para a linha            
            linha.append(valor)               
        tabela.append(linha)   
    return tabela,pedra,pote
#---------------------------
# FUNÇÃO MAIN
#---------------------------
def main(): 

  for w in range(1): 
      pedra,pote = recebe_valores()
      pedra,pote = valida_dados(pedra,pote)  
      gera_tabela(tabela,pedra,pote) 
      tabela_organizada = [] # TABELA ONDE ARMAZENA OS DADOS ORGANIZADOS
      for k in range(len(tabela)):
        if sum(tabela[k]) == pedra: # FILTRA CADA LINHA SOMATORIO DE CADA LINHA IGUAL AO NUMERO DE PEDRAS
          tabela_organizada.append(tabela[k])
          a = np.array(tabela_organizada)

  print("TABELA COM AS MANEIRAS QUE JOÃOZINHO PODE ORGANIZAR SUAS PEDRAS:")        
  print(np.unique(a, axis=0))
  print("Quantidade de maneiras possiveis: {}".format(len(np.unique(a, axis=0))))
if __name__ == "__main__":
  main()
