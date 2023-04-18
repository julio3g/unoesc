!pip install simple-colors

from simple_colors import *
##3.5 milhões o usuario possui. 


opcoes = [
{
    'cod': 1,
    'metodo': 'Dinamite',
    'valor': 200000
},
{
    'cod': 2,
    'metodo': 'Minhocas Radioativas',
    'valor': 2500000
},
{
    'cod': 3,
    'metodo': 'Retroescavadeira',
    'valor': 500000
},
{
    'cod': 4,
    'metodo': 'Empurradores',
    'valor': 1800000
},
{
    'cod': 5,
    'metodo': 'Imãs',
    'valor': 1000000
},
{
    'cod': 6,
    'metodo': 'Fiat Uno de Firma',
    'valor': 22000 + 6.662*10000
},
{
    'cod': 7,
    'metodo': 'peixinhos',
    'valor': 200000
},
{
    'cod': 8,
    'metodo': 'rebocadores',
    'valor': 2500000
},
{
    'cod': 9,
    'metodo': 'Noé',
    'valor': 0
},                 
]
sair = False
opcao = ''

while sair == False:
  print("********************************Operação Suez********************************")
  for i in opcoes:
      if escolha == i['cod']:
        opcao = i
  escolha = int(input("-Detectamos nos nossos sistemas que o navio atingiu um grande banco de areia em uma das margens, encalhando o navio. Você tem limite de 6,5mi.\nO que deseja fazer? Opções:\n1-Usar dinamite para fazer o banco de areia ceder(R$100.000,00).\n2-Usar minhocas biologicamente modifcadas para comer a areia(R$2mi)\n3-Usar retroescavadeiras para mover a areia para outro lugar(R$20.000,00)\n"))
  
  if escolha == 1:
    print(green('Muito bem! Você tomou a melhor decisão.', 'bold'))
    sair = True   
    for i in opcoes:
      if escolha == i['cod']:
        opcao = i
    escolha = int(input("-Conseguimos desatolar o navio. Agora precisamos fazer com que ele volte a sua posição original para seguir caminho. Qual será sua próxima decisão?\n4-Usar imãs gigantes.\n5-Usar empurradores.\n6-Amarrar um Fiat Uno Mile Fire 2002 Álcool de firma com escada de aluminio para tirar o navio do canal(R$11.200,00 + 6,550 por litro).\n"))
    
    if escolha == 4:
      print('Ta assistindo muito velozes e furiosos.')
    
    if escolha == 5:
      print('Parabéns! Certamente você tomou a decisão correta.')
      
      for i in opcoes:
        if escolha == i['cod']:
          opcao = i
          
      escolha = int(input("-Conseguimos centralizar o navio. Agora precisamos fazer com que ele volte a navegar, decida o que vamos fazer agora.\n7-350 peixinhos dourados amarrados no navio.(R$10.000)\n8-Usar rebocadores para tracionar o navio, fazendo com que ele pegue no tranco.\n9-Aguardar o dilúvio.(120000 anos).\n"))
      if escolha == 7:
        print("Provavelmente você terá problemas com Ibama, aguarde o processo.")
      if escolha == 8:
        print("Parábens! Você não fudeu com a economia mundial.")
      if escolha == 9:
        print("Genênis 7:17")
    
    if escolha == 6:
      print("Opção inviavel devido ao alto custo do Álcool e a dificuldade de encontrar um uno no deserto.")
  if escolha == 2:
    print(red('Incorreta! Volte pro 6º ano.', 'bold'))
  if escolha == 3:
    print(red('No ano de 2077 o serviço foi terminado. Parabéns pelos netos.', 'bold'))
 
      
      
    
