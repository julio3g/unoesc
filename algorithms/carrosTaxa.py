car_value = float(input('Qual o valor de fábrica do veículo?'))
shop_value = car_value*0.28
tax_value = car_value*0.45
final_value = car_value + shop_value + tax_value
print('Seu carro custará:',final_value)
