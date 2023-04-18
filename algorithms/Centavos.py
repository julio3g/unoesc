centavos = int(input())
real1 = centavos // 100
sobra1 = (centavos/100) - real1
real50 = int(sobra1//0.5)
sobra2 = sobra1 - 0.5
real10 = int(sobra2//0.1)
sobra3 = sobra2 - 0.1
real5 = round(sobra3/0.05)

if(centavos%100 == 0):
  print('Você precisará de', real1, 'moedas de 1 real')
if(sobra1 > 0):
  
  print('Você precisará de', real1, 'moedas de 1 real')
  print('Você precisará de', real50, 'Moedas de 50 centavos')
if(sobra2 >= 0):
  print('Você precisará de', real1, 'moedas de 1 real')
  print('Você precisará de', real50, 'Moedas de 50 centavos')
  print('Você precisará de', real10, 'moedas de 10 centavos')

