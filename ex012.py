preco = float(input('Preço do produto: R$'))
calc = preco * (5/100)
desc = preco - calc
print('O produdo de R${} com 5% de desconto fica R${:.2f}'.format(preco, desc))
