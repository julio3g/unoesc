import random

def criar_matriz(num_linhas, num_colunas):
  matriz = []
  for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
      x = random.randint(0,5)
      linha.append(x)
    matriz.append(linha)
  return matriz
matriz = criar_matriz(10,20)
print(f'Matriz Principal: {matriz}')
somas = []

for l in range(10):
  for c in range(1):
    a = matriz[l][0]
    b = matriz[l][1]
    v = matriz[l][2] ##ESSE É O C
    d = matriz[l][3]
    e = matriz[l][4]
    f = matriz[l][5]
    g = matriz[l][6]
    h = matriz[l][7]
    i = matriz[l][8]
    j = matriz[l][9]
    k = matriz[l][10]
    t = matriz[l][11] ##ESSE É O L
    m = matriz[l][12]
    n = matriz[l][13]
    o = matriz[l][14]
    p = matriz[l][15]
    q = matriz[l][16]
    r = matriz[l][17]
    s = matriz[l][18]
    u = matriz[l][19]
    soma = a + b + v + d + e + f + g + h + i + j + k + t + m + n + o + p + q + r + s + u
    somas.append(soma)
print(f'Somas de cada Linha: {somas}')


def criar_matrizR(num_linhas, num_colunas):
  R = []
  for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
      x = 0
      linha.append(x)
    R.append(linha)
  return R
R = criar_matrizR(10,20)


for l in range(10):
  for c in range(20):
    Multi = (matriz[l][c] * somas[l])
    R[l][c] = Multi
print(f'Matriz resutalnte:{R}')
