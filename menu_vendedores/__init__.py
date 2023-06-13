import matplotlib.pyplot as plt

def menu():
    print('1 - Alterar Dados.')
    print('2 - Cadastrar produto.')
    print('3 - Buscar produto.')
    print('4 - Remover produto.')
    print('5 - Atualizar produto.')
    print('6 - Gerar Grafico.')
    print('7 - Gerar arquivo txt dos produtos')
    print('0 - Sair.')

    print(53 * '=')
    opcao = input('Digite a opcao desejada: ')
    print(53 * '=')

    return opcao

def alterar_dados (login,vendedores:dict):
    while True:
        print('Digite 0 - para sair')
        print('Digite 1 - para alterar nome')
        print('Digite 2 - para alterar email')
        print('Digite 3 - para alterar senha')

        print(53 * '=')
        op_alterar_dados = input('Digite a opcao: ')
        print(53 * '=')

        if op_alterar_dados == '0':
            break
        elif op_alterar_dados == '1':
            print(f'Nome Atual: {vendedores[login][0]}')
            novo_nome = input('Digite o novo nome: ')
            vendedores[login][0] = novo_nome
            print('Novo nome alterado com Sucesso')
            break
        elif op_alterar_dados == '2':
            print(f'Email atual: {vendedores[login][3]}')
            while True:
                while True:
                    novo_email = input('Digite seu novo Email:')
                    if novo_email.count('@gmail.com') == 1 or novo_email.count('@hotmail.com') == 1:
                        break
                    else:
                        print('\033[0;30;41m Email invalido, tente novamente. \033[m')
                email_ja_cadastrado = False
                for dados in vendedores.values():
                    if dados[3] == novo_email:
                        email_ja_cadastrado = True
                        print('\033[0;30;41m Email já cadastrado, tente novamente. \033[m')
                        break
                if not email_ja_cadastrado:
                    break
            vendedores[login][3] = novo_email
            print('Email alterado com sucesso')
        elif op_alterar_dados == '3':
            nova_senha = input('Digite a nova senha: ')
            vendedores[login][1] = nova_senha
        else:
            print('Opcao Invalida')
            
def cadastrar_produto(login,produtos:dict):
    lista_produto = []
    while True:
        nome_produto = input('Digite o nome do produto: ')
        produto_ja_cadastrado = False
        for produto in produtos.values():
            if produto[0] == login:
                if produto[1] == nome_produto:
                    print('Nome de produto já cadastrado.')
                    produto_ja_cadastrado = True
                    break
        if not produto_ja_cadastrado:
            break

    while True:
        id_produto = int(input('Digite o ID do produto: '))
        produto_ja_cadastrado = False
        for produto in produtos.values():
            if produto[0] == login:
                if produto[7] == id_produto:
                    print('ID de produto já cadastrado.')
                    produto_ja_cadastrado = True
                    break
        if not produto_ja_cadastrado:
            break
    while True:
        estoque = int(input('Digite o estoque do produto: '))
        if estoque >= 0:
            break
        else:
            print('\033[0;30;41m Estoque deve ser maior ou igual a 0. \033[m')
    fabricacao_produto = int(input('Digite o ano de fabricacao do produto: '))
    while True:
        validade_produto = int(input('Digite o ano de validade do produto: '))
        if validade_produto >= fabricacao_produto:
            break
        else:
            print('\033[0;30;41m Ano de validade do produto deve ser maior que o ano de fabricao. \033[m')
    while True:
        preco_produto = float(input('Digite o preco do produto: '))
        if preco_produto >= 0:
            break
        else:
            print('\033[0;30;41m Preço do produto deve ser maior ou igual a 0. \033[m')
    descricao = input('Digite a descricao do produto: ')

    lista_produto.append(login)  # 0
    lista_produto.append(nome_produto)  # 1
    lista_produto.append(estoque)  # 2
    lista_produto.append(fabricacao_produto)  # 3
    lista_produto.append(validade_produto)  # 4
    lista_produto.append(preco_produto)  # 5
    lista_produto.append(descricao)  # 6
    lista_produto.append(id_produto)  # 7
    produtos[id_produto] = lista_produto

    print(f'\nProduto: {nome_produto}\nEstoque: {estoque}\nID: {id_produto}\nAno de fabricacao: {fabricacao_produto}\nData de Validade do produto: {validade_produto}\nPreco: {preco_produto}\n')

    print('==================== Produto cadastrado com sucesso! ====================')

def buscar_produtos (login,produtos:dict):
    busca_produto = input('Digite o nome para buscar o produto: ')
    buscado = False
    for produto in produtos.values():
        if produto[0] == login:
            if produto[1].find(busca_produto) >= 0:
                buscado = True

                print(53 * '=')
                print(f'Id: {produto[7]}')
                print(f'Nome do produto: {produto[1]}')
                print(f'Estoque: {produto[2]}')
                print(f'Ano de Fabricacao: {produto[3]}')
                print(f'Validade: {produto[4]}')
                print(f'Preco: {produto[5]}')
                print(f'Descricao: {produto[6]}\n\n')
                print(53 * '=')

    if not buscado:
        print('\033[0;30;41m Produto nao encontrado. \033[m')

def remover_produto (login,produtos:dict):
    remocao = False
    id_remove = int(input('Digite o ID do produto para remocao: '))
    for produto in produtos.values():
        if produto[0] == login:
            if produto[7] == id_remove:
                produtos.pop(id_remove)
                remocao = True
                print('Produto removido com sucesso')
                break
        if remocao:
            break
    if not remocao:
        print('\033[0;30;41m Produto nao encontrado. \033[m')

def atualizar_produto (login,produtos:dict):
    achado = False
    id_atualiza = int(input('Digite o ID do produto para Atualizar: '))
    for produto in produtos.values():
        if produto[0] == login:
            if produto[7] == id_atualiza:
                achado = True

                print(53 * '=')
                print('nome: ', produtos[id_atualiza][1])
                print('Id: ', produtos[id_atualiza][7])
                print('Estoque: ', produtos[id_atualiza][2])
                print('Ano de Fabricacao: ', produtos[id_atualiza][3])
                print('Validade: ', produtos[id_atualiza][4])
                print('Preco: ', produtos[id_atualiza][5])
                print('Descricao: ', produtos[id_atualiza][6], '\n')
                print(53 * '=')

             
                print('Digite 0 - sair')
                print('Digite 1 - Atualizar nome')
                print('Digite 2 - Atualizar estoque')
                print('Digite 3 - Atualizar ano de fabricacao')
                print('Digite 4 - Atualizar Validade')
                print('Digite 5 - Atualizar Preco')
                print('Digite 6 - Atualizar descricao')
                
                print(53 * '=')
                op_atualizar = input('Digite a opcao: ')
                print(53 * '=')

                if (op_atualizar) == '0':
                    break
                elif (op_atualizar) == '1':
                    novo_nome = input('Digite o novo nome: ')
                    produtos[id_atualiza][1] = novo_nome
                elif (op_atualizar == '2'):
                    novo_estoque = int(input('Digite o novo estoque: '))
                    if (novo_estoque >= 0):
                        produtos[id_atualiza][2] = novo_estoque
                        break
                    else:
                        print('\033[0;30;41m Estoque deve ser maior ou igual a 0. \033[m')
                elif (op_atualizar == '3'):
                    novo_ano_de_fab = int(input('Digite o novo ano de fabricacao: '))
                    produtos[id_atualiza][3] = novo_ano_de_fab
                elif (op_atualizar == '4'):
                    nova_validade = int(input('Digite a nova validade: '))
                    produtos[id_atualiza][4] = nova_validade
                elif (op_atualizar == '5'):
                    novo_preco = float(input('Digite o novo preco: '))
                    if novo_preco >= 0:
                        produtos[id_atualiza][5] = novo_preco
                        break
                    else:
                        print('\033[0;30;41m Preco deve ser maior ou igual a 0. \033[m')
                elif (op_atualizar == '6'):
                    nova_descricao = input('Digite a nova descricao: ')
                    produtos[id_atualiza][6] = nova_descricao
                else:
                    print('Opcao Invalida')
    if not achado:
        print('\033[0;30;41m Produto nao encontrado. \033[m')


def gerar_grafico (login,produtos:dict):
    data = {}
    for produto in produtos.values():
        if produto[0] == login:
            data[produto[1]] = produto[2]
    courses = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(10, 5))
    plt.bar(courses, values, color='maroon', width=0.4)
    plt.xlabel("Produtos")
    plt.ylabel("Quantidade")
    plt.title("Sertao Livre")
    plt.show()


def salvarArquivo(texto, login):

    f = open(f'produtos_{login}.txt', 'w')
    f.write(texto)
    f.close()


def salvarprodutos(login,produtos:dict):
    texto = ''
    for cod in produtos:
        if produtos[cod][0] == login:
            texto += (f'nome do produto: {produtos[cod][1]}\n')
            texto += (f'valor do produto: {produtos[cod][5]}\n')
            texto += (f'qtde do produto: {produtos[cod][2]}\n\n')

    salvarArquivo(texto, login)