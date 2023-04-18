!pip install simple-colors
from simple_colors import *
import numpy as np

print(yellow('Bem-vindos à Segunda Grande Guerra. Onde só os mais fortes sobrevivem! Embarque conosco nessa aventura e vamos afundar alguns navios.\nCapitão tivemos informações recentes de que um ataque aconteceria no Golfo de Leyte no dia 23/10/1944 em torno de sua ilha, localizada nas Filipinas.\nMontamos uma frota marítima de 5 navios de guerra, podemos posiciona-los independentementes ao longo de um raio de 8km².\nMas primeiro precisamos da assinatura de quem irá comandar esta operação: ', ['bold']))
print(black("Assine aqui: ", ['bold']))
jogador_1 = input()
print(cyan('CAPITÃO! CAPITÃO! Um ataque eminente está para começar em torno da Ilha de Leyte,\nas tropas inimigas estão para se posicionar devemos nos organizar para deferder nosso território!\nMas primeiro precisamos de sua autorização',['bold']))
print(black("Assine aqui: ", ['bold']))
jogador_2 = input()

def criar_matriz(num_linhas, num_colunas):
  matriz = []
  for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
      linha.append('O')
    matriz.append(linha)
  return matriz

tabuleiro_1 = np.array(criar_matriz(8,8))
tabuleiro_2 = np.array(criar_matriz(8,8))

##for l in tabuleiro_1:
  ##print('  '.join(map(str,l)))


print("=-"*12)

def Posicao1(jogada1):
  while jogada1 > 0:
    c = int(input("Insira um valor para X: ")) - 1
    l = int(input("Insira um valor para Y: ")) - 1
    if c <= 7 and l <= 7:
      if tabuleiro_1[c][l] != "X":
          tabuleiro_1[l][c] = "X"
          jogada1 -= 1
      else:
        print(red("Você já colocou ai"))
    else:
      print(red("Número inválido!"))

def Posicao2(jogada2):
  while jogada2 > 0:
    c = int(input("Insira um valor para X: ")) - 1
    l = int(input("Insira um valor para Y: ")) - 1
    if c <= 7 and l <= 7:
      if tabuleiro_2[c][l] != "X":
          tabuleiro_2[l][c] = "X"
          jogada2 -= 1
      else:
        print(red("Você já colocou ai"))
    else:
      print(red("Número inválido!"))
#Aqui o jogador declara a posição dos barcos

print(yellow(f"      Cap.{jogador_1}      "))
barcos = Posicao1(5)
for l in tabuleiro_1:
  print(blue('  '.join(map(str,l))))
print("=-"*12)

pronto = input(f"{jogador_1} coloce x para continuar.")
if pronto == "x" or pronto == "X":
  print(".\n"*100)

#print(".\n"*100)

print(cyan(f"      Cap.{jogador_2}      "))
barcos = Posicao2(5)

for l in tabuleiro_2:
  print(blue('  '.join(map(str,l))))
print("=-"*12)

pronto = input(f"{jogador_2} coloce x para continuar.")
if pronto == "x" or pronto == "X":
  print(".\n"*100)

#print(".\n"*100)

#JOGO

barcos = [5,5]
def Jogar1():
  if barcos[1] > 0:
    l = int(input("Qual posição X deseja atacar?")) - 1
    c = int(input("Qual posição Y deseja atacar?")) - 1
    if tabuleiro_2[c][l] == 'A':
      print("Você já atacou ai")
    if tabuleiro_2[c][l] == 'B':
      print("Você já atacou ai")  
    if tabuleiro_2[c][l] == 'O':
      print(blue('************* ÁGUA ************',  ['bold', 'underlined']))
      tabuleiro_2[c][l] = "A"      
    if tabuleiro_2[c][l] == 'X':
      print(red('************ BOMBA ************', ['bold', 'underlined']))
      tabuleiro_2[c][l] = "B"
      barcos[1] -= 1
      print(green(f'Restam {barcos[1]} barcos inimigos'))
    if barcos[1] == 0:
      print("Parabéns! Você ganhou.")
  else:
    print(green("Parabéns! Conseguimos vencer a guerra e conquistamos a ilha."))


def Jogar2():
  if barcos[0] > 0:
    l = int(input("Qual posição X deseja atacar?")) - 1
    c = int(input("Qual posição Y deseja atacar?")) - 1
    if tabuleiro_1[c][l] == 'A':
      print("Você já atacou ai")
    if tabuleiro_1[c][l] == 'B':
      print("Você já atacou ai")
    if tabuleiro_1[c][l] == 'O':
      print(blue('************* ÁGUA ************', ['bold', 'underlined']))
      tabuleiro_1[c][l] = "A"
    if tabuleiro_1[c][l] == 'X':
      print(red('************ BOMBA ************', ['bold', 'underlined']))
      tabuleiro_1[c][l] = "B"
      barcos[0] -= 1
      print(green(f'Restam {barcos[0]} barcos inimigos'))
  else:
    print(green("Parabéns! Vencemos, mostramos nossa sobenaria perante nossos territórios."))


jogadores = [1,2]

for l in range(8):
  for c in range(8):
    for i in range(2):
      a = jogadores[i]
      barcos1 = barcos[0]
      barcos2 = barcos[1]
      if barcos1 > 0 and barcos2 > 0:  
        if a == 1:
          print(yellow(f"      Cap.{jogador_1}      "))
          z = Jogar1()
        else:
          print(blue(f"      Cap.{jogador_2}      "))
          ç = Jogar2()
