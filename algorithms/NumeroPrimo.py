numeros = []
primos = []
nao_primos = []
limite = 0

while(limite < 9):
  numero = int(input("Qual número deseja adicionar?"))
  numeros.append(numero)
  pos = numeros.index(numero)
  limite += 1
  dividendo1 = 2
  conta1 = numero % dividendo1
  dividendo2 = 5
  conta2 = numero % dividendo2
  if(numero == 1):
    print("Esse número não é primo")
    nao_primos.append(numero)
  elif(conta1 != 0 and conta2 != 0 or numero == 2):
    print("Esse número é primo")
    primos.append(numero)
  else: 
    print("Esse número não é primo")
    nao_primos.append(numero)

print(f"Numeros={numeros}")
print(f"Primos={primos}")
print(f"Não primos={nao_primos}")


  


