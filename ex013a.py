preco = float(input('Qual é o preço do produto: R$'))
avista = preco - (preco * 10/100)
print('O produto de R${} á vista  com 10% de desconto fica R${}'.format(preco, avista))
parcelado = preco + (preco * 8/100)
print('O produto de R${} parcelado com aumento de 8% fica R${}'.format(preco, parcelado))
