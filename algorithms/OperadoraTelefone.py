hori = int(input("Qual foi a hora de ínicio:"))
mini = int(input("Qual foi o minuto de ínicio:"))
horf = int(input("Qual foi a hora de término:"))
minf = int(input("Qual foi o minuto de término:"))

ligacao = 1

ini = hori * 60 + mini
fim = horf * 60 + minf

total = fim - ini

print(f'Tempo total de duração da chamada: {total} minutos')

if hori >= 0 and hori <= 9:
  if horf >= 0 and horf <= 9:
    desc = 0.5
    valor = total * desc
    print(f"O valor total a ser pago será de: {valor}")
  elif horf > 9 and horf <=18:
    norm = fim - 9 * 60 
    desc = 9 * 60 - ini
    valor_desc = desc * (ligacao * 0.5)
    totalig = norm + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')
  elif horf > 18 and horf <= 21:
    norm = fim - 18 * 60 #60
    desc = 18 * 60 - ini #540
    valor_desc = norm * 0.5
    totalig = desc + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')
  elif horf > 21 and horf <= 23:
    norm = fim - 21 * 60 #0
    desc = (21 * 60 - ini)*0.3 #234
    x = (21*60 - ini) - desc
    valor_desc = norm * 0.5
    totalig = x + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')

if hori > 9 and hori <= 18:
  if horf >= 9 and horf <= 18:
    
    valor = total
    print(f"O valor total a ser pago será de será de: {valor}")
  elif horf > 9 and horf <=18:
    norm = fim - 9 * 60 
    desc = 9 * 60 - ini
    valor_desc = desc * ligacao
    totalig = norm + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')
  elif horf > 18 and horf <= 21:
    norm = fim - 18 * 60 #60
    desc = 18 * 60 - ini #540
    valor_desc = norm 
    totalig = desc + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')
  elif horf > 21 and horf <= 23:
    norm = fim - 21 * 60 #0
    desc = (21 * 60 - ini) #234
    x = (21*60 - ini) - desc
    valor_desc = norm 
    totalig = x + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')

if hori > 18 and hori <= 21:
  desc = 0.3
  if horf >= 18 and horf <= 21:
    desc = 0.3
    valor = total * desc
    print(f"O valor total a ser pago será de: {valor}")
  elif horf > 9 and horf <=18:
    norm = fim - 9 * 60 
    desc = 9 * 60 - ini
    valor_desc = desc * (ligacao * 0.5)
    totalig = norm + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')
  elif horf > 18 and horf <= 21:
    norm = fim - 18 * 60 
    desc = 18 * 60 - ini 
    valor_desc = norm * 0.5
    totalig = desc + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')
  elif horf > 21 and horf <= 23:
    norm = fim - 21 * 60 
    desc = (21 * 60 - ini)*0.3 
    x = (21*60 - ini) - desc
    valor_desc = norm * 0.3
    totalig = x + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')

if hori > 21 and hori <= 23 and mini <= 59:
  desc = 0.4
  if horf >= 21 and horf <= 23:
    desc = 0.4
    descreal = total * desc
    valor = total - descreal
    print(f"O valor total a ser pago será de será de: {valor}")
  elif horf > 9 and horf <=18:
    norm = fim - 9 * 60 
    desc = 9 * 60 - ini
    valor_desc = desc * (ligacao * 0.4)
    totalig = norm + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')
  elif horf > 18 and horf <= 21:
    norm = fim - 18 * 60 #60
    desc = 18 * 60 - ini #540
    valor_desc = norm * 0.4
    totalig = desc + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')
  elif horf > 21 and horf <= 23:
    norm = fim - 21 * 60 #0
    desc = (21 * 60 - ini)*0.4 #234
    x = (21*60 - ini) - desc
    valor_desc = norm * 0.4
    totalig = x + valor_desc
    print(f'O valor total a ser pago será de: {totalig}')
