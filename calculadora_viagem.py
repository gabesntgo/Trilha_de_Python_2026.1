orcamento = float(input('Digite o valor do orçamento, em reais: '))
destino = str(input('Digite o destino da viagem: '))
custo_passagem = float(input('Digite o valor da passagem, em reais: '))
custo_diaria = float(input('Digite o valor da diaria, em euros: '))
dias = int(input('Quantos dias durará a viagem? '))

hospedagem = custo_diaria * 6.10 * dias
total = custo_passagem + hospedagem

if orcamento <= 0 or custo_diaria <= 0 or dias <= 0:
    raise ValueError('Insira valores válidos')


if total <= orcamento:
    print('O valor da hospedagem total, em reais, é: ', hospedagem)
    print('O valor total da viagem, em reais, é: ', total)
    print('Viagem para', destino, 'é possível! Sobrarão', orcamento - total, 'reais!')
else:
    print('O valor da hospedagem total, em reais, é: ', hospedagem)
    print('O valor total da viagem, em reais, é: ', total)
    print('Viagem para', destino, 'é impossível! Faltam', total - orcamento, 'reais!')
