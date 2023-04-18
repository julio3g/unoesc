##Faça um programa que preencha uma matriz M (2 X 2), calcule e mostre a matriz R, resultante da multiplicação dos elementos de M pelo seu maior elemento

matriz = [[0,0],[0,0]]
maior = 0
for l in range (0,2):
  for c in range (0,2):
    matriz[l][c] = int(input(f'Insira o valor para [{l},{c}]:'))
print(f"Matriz Principal:{matriz}")

maior = matriz[0][0]
for l in range(0,2):
    for c in range(0,2):        
      if maior < matriz[l][c]:
          maior = matriz[l][c]
  
R = [[0,0],[0,0]]
for l in range(0,2):
  for c in range(0,2):
    Multi = matriz[l][c] * maior
    R[l][c] = Multi
print(f"Matriz R:{R}")
       
