fila = ['danilo', 'mateus', 'berlofa', 'davi']

while True:
    print(f'A lista tem: {fila}')
    adicionar = input('Digite: 0 para sair / 1 para adicionar / 2 para tirar:')

    if adicionar == '1':
        adicionar = input('Digite o nome de quem deseja adicionar:')
        if adicionar == "":
            print('nome inválido')
        else:
            fila.append(adicionar)
    if adicionar == '2':
        print(f'Pessoas da fila: {fila}')
        adicionar = int(input('Digite a posição de quem deseja tirar da lista:'))
        if adicionar == "":
            print('nome inválido')
        else:
            fila.pop(adicionar - 1)
    if adicionar == '0':
        break
