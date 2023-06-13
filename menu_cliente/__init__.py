import openai

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

def alterar_dados (login, clientes:dict):
    while True:
        print('Digite 0 para sair')
        print('Digite 1 para alterar nome')
        print('Digite 2 para alterar email')
        print('Digite 3 para alterar senha')

        print(53 * '=')
        op_alterar_dados = input('Digite a opcao: ')
        print(53 * '=')

        if op_alterar_dados == '0':
            break
        elif op_alterar_dados == '1':
            print(f'Nome Atual: {clientes[login][0]}')
            novo_nome = input('Digite o novo nome: ')
            clientes[login][0] = novo_nome
            print('Novo nome alterado com Sucesso')
            break
        elif op_alterar_dados == '2':
            print(f'Email atual: {clientes[login][3]}')
            while True:
                while True:
                    novo_email = input('Digite seu novo Email:')
                    if novo_email.count('@gmail.com') == 1 or novo_email.count('@hotmail.com') == 1:
                        break
                    else:
                        print('\033[0;30;41m Email invalido, tente novamente. \033[m')
                email_ja_cadastrado = False
                for dados in clientes.values():
                    if dados[3] == novo_email:
                        email_ja_cadastrado = True
                        print('\033[0;30;41m Email já cadastrado, tente novamente. \033[m')
                        break
                if not email_ja_cadastrado:
                    break
            clientes[login][3] = novo_email
            print('Email alterado com sucesso')
        elif op_alterar_dados == '3':
            nova_senha = input('Digite a nova senha: ')
            clientes[login][1] = nova_senha
        else:
            print('Opcao Invalida')

def buscar_produto (login,produtos:dict,compras:dict):
    busca_produto = input('Digite o nome para buscar o produto: ')
    buscado = False
    for produto in produtos.values():
        if produto[1].find(busca_produto) >= 0 or produto[6].find(busca_produto) >= 0:
            buscado = True

            print(53 * '=')
            print(f'Id: {produto[7]}')
            print(f'Nome do produto: {produto[1]}')
            print(f'Estoque: {produto[2]}')
            print(f'Ano de Fabricacao: {produto[3]}')
            print(f'Validade: {produto[4]}')
            print(f'Preco: R${produto[5]}')
            print(f'Descricao: {produto[6]}\n')
            print(53 * '=')

    if not buscado:
        print('\033[0;30;41m Produto nao encontrado. \033[m')
    else:
        while True:
            print('Digite 0 - sair')
            print('Digite 1 - comprar um produto')

            opcao_venda = input('Digite a opcao desejada: ')

            if (opcao_venda == '0'):
                break
            if opcao_venda == '1':
                
                id_procurado = int(input('Digite o codigo do produto desejado: '))
                achado = False
                for produto in produtos.values():
                    if produto[7] == id_procurado:
                        achado = True
                        quantidade_comprada = int(input('Digite a quantidade q voce deseja comprar: '))
                        if produto[2] <= quantidade_comprada:
                            print(f'Quantidade desejada para comprar:{quantidade_comprada} deve ser menor ou igual ao estoque: {produto[2]}')
                        else:
                            valor = produto[5] * quantidade_comprada
                            print(f'Preco total da quantidade desejada:R${valor}')
                            pago = float(input('Digite o Valor pago: '))

                            if valor > pago:
                                print(f'Valor pago: R${pago} deve ser maior ou igual ao preço do produto: R${valor}')
                            else:
                                troco = pago - valor
                                if troco > 0:
                                    print(f'Seu troco: R${troco}')

                                produto[2] -= quantidade_comprada
                                ja_comprado = False
                                for compra in compras.values():
                                    if compra[3] == login:
                                        if compra[0] == produto[1]:
                                            ja_comprado = True
                                            compra[1] += quantidade_comprada
                                            compra[2] += valor
                                            break
                                if not ja_comprado:
                                    lista_compras = []
                                    lista_compras.append(produto[1])  
                                    lista_compras.append(quantidade_comprada)  
                                    lista_compras.append(valor)  
                                    lista_compras.append(login)  
                                    compras[produto[1]] = lista_compras
                                    break
                if not achado:
                    print('\033[0;30;41m Produto não encontrado. \033[m')
            else:
                print('Opcao Invalida')
def compras_feitas (login,compras:dict):
    compra_feita = False
    for compra in compras.values():
        if compra[3] == login:
            compra_feita = True
            print(53 * '=')
            print(f'Produto comprado: {compra[0]}')
            print(f'Quantidade comprada: {compra[1]}')
            print(f'Valor Gasto total: {compra[2]}')
            print(53 * '=')

    if not compra_feita:
        print('\033[0;30;41m Nenhuma compra feita. \033[m')

def consultarchatgpt(nome_produto):
    openai.api_key = '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'

    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = 'Faça uma descricao resumida de' + nome_produto
    # Set the maximum number of tokens to generate in the response
    max_tokens = 1024

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    return completion.choices[0].text
import menu_cliente
def gpt_consulta (produtos:dict):
    busca_produto = input('Nome do produto: ')
    buscado = False
    for produto in produtos.values():
        if produto[1].find(busca_produto) >= 0:
            buscado = True
            print(f'Codigo do produto: {produto[7]}')
            print(f'Nome do produto: {produto[1]}')
    if not buscado:
        print('\033[0;30;41m Produto nao encontrado. \033[m')
    else:
        codigo_buscado = int(input('Digite o codigo do produto q voce deseja ver decricao: '))
        for produto in produtos.values():
            if produto[7] == codigo_buscado:
                produto_nome = produto[1]
                print(menu_cliente.consultarchatgpt(produto_nome))