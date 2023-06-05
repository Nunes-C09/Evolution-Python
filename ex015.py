dias = int(input('Quantidade de dias alugado: '))
km = float(input('Quantidade de km precorrido: '))
preco = (dias * 60) + (km * 0.15)
'''kmr = km * 0.15
preco = diar + kmr'''
print('O preço a pagar é de R${:.2f}'.format(preco))

