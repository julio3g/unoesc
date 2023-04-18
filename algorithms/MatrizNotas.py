import random
notas = [
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]
]

for l in range(0,10):
  for c in range(0,3):
    x = random.randint(0,10)
    notas[l][c] = x

prova_um = 0
prova_dois = 0
prova_tres =0
for l in range(0,10):
  for c in range(0,1):  
    d = notas[l][0]
    e = notas[l][1]
    f = notas[l][2]
    if d<e and d<f:
      menor = d
      prova = 1
    if e<d and e<f:
      menor = e
      prova = 2
    if f<d and f<e:
      menor = f
      prova = 3
    if prova == 1:
      prova_um += 1
    if prova == 2:
      prova_dois += 1
    if prova == 3:
      prova_tres += 1
    print(f'Aluno {l} | Menor nota:{menor} | Prova: {prova}')
print(f'Piores notas em cada prova:\nProva 1: {prova_um}\nProva 2: {prova_dois}\nProva 3: {prova_tres}')
 
