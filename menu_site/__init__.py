def menu ():
  
    print('================== SEJA BEM VINDO! ==================')
    print('1 - Quero me tornar um vendedor')
    print('2 - Quero me tornar um cliente')
    print('3 - Realizar Login')
    print('0 - Sair')
    
    print(53 * '=')
    opcao = input('Digite a opcao desejada: ')
    print(53 * '=')

    return opcao

def cadastrar_vendedores (geral:dict,vendedores:dict,clientes:dict):
    while True:
        existe = False
        login = input('Crie seu login: ')
        for dv in vendedores.keys():
            if login == dv:
                existe = True
                break
        for dv in clientes.keys():
            if login == dv:
                existe = True
                break
        if not existe:
            break
        else:
            print('\033[0;30;41m O login ja existe, tente outro. \033[m')

    while True:
        senha = input('Digite uma senha: ')
        if (senha == login):
            print('\033[0;30;41m Sua senha precisa ser diferente do login, tente novamente. \033[m')
            continue
        break

    nome_vendedor = input('Digite seu nome: ')
    while True:
        cpf_vendedor = input('Digite seu CPF: ')
        if len(cpf_vendedor) != 11:
            print('\033[0;30;41m CPF inválido. Digite apenas 11 números. \033[m')
        else:
            cpf_ja_cadastrado = False
            for usuario in vendedores.values():
                if usuario[2] == cpf_vendedor:
                    cpf_ja_cadastrado = True
                    print('\033[0;30;41m CPF já cadastrado, tente novamente. \033[m')
                    break
            if not cpf_ja_cadastrado:
                break

    while True:
        while True:
            email_vendedor = input('Digite o email: ')
            if email_vendedor.count('@gmail.com') == 1 or email_vendedor.count('@hotmail.com') == 1:
                break
            else:
                print('\033[0;30;41m Email invalido, tente novamente. \033[m')

        email_ja_cadastrado = False
        for usuario in vendedores.values():
            if usuario[3] == email_vendedor:
                email_ja_cadastrado = True
                print('\033[0;30;41m Email já cadastrado, tente novamente. \033[m')
                break
        if not email_ja_cadastrado:
            break
    lista = []
    lista.append(nome_vendedor)
    lista.append(senha)
    lista.append(cpf_vendedor) 
    lista.append(email_vendedor) 
    lista.append(login) 
    geral[login] = 'vendedor'
    vendedores[login] = lista
    print(f'====================== {nome_vendedor} VOCE AGORA É UM VENDEDOR DO SERTÃO LIVRE! ======================')

def cadastrar_cliente (geral:dict,clientes:dict,vendedores:dict):
    while True:
        existe = False
        login = input('Crie seu login: ')
        for dv in clientes.keys():
            if login == dv:
                existe = True
                break
        for dv in vendedores.keys():
            if login == dv:
                existe = True
                break
        if not existe:
            break
        else:
            print('\033[0;30;41m O login ja existe, tente outro. \033[m')

    while True:
        senha = input('Digite uma senha: ')
        if (senha == login):
            print('\033[0;30;41m ERRO, sua senha precisa ser diferente do login, tente novamente. \033[m')
            continue
        break

    nome_cliente = input('Digite seu nome: ')
    while True:
        cpf_cliente = input('Digite seu CPF: ')
        if len(cpf_cliente) != 11:
            print('\033[0;30;41m CPF inválido. Digite apenas 11 números. \033[m')
        else:
            cpf_ja_cadastrado = False
            for usuario in clientes.values():
                if usuario[2] == cpf_cliente:
                    cpf_ja_cadastrado = True
                    print('\033[0;30;41m CPF já cadastrado, tente novamente. \033[m')
                    break
            if not cpf_ja_cadastrado:
                break

    while True:
        while True:
            email_cliente = input('Digite o email: ')
            if email_cliente.count('@gmail.com') == 1 or email_cliente.count('@hotmail.com') == 1:
                break
            else:
                print('\033[0;30;41m Email invalido, tente novamente. \033[m')

        email_ja_cadastrado = False
        for usuario in clientes.values():
            if usuario[3] == email_cliente:
                email_ja_cadastrado = True
                print('\033[0;30;41m Email já cadastrado, tente novamente. \033[m')
                break
        if not email_ja_cadastrado:
            break
    lista = []
    lista.append(nome_cliente) 
    lista.append(senha) 
    lista.append(cpf_cliente)  
    lista.append(email_cliente)  
    lista.append(login)  
    geral[login] = 'cliente'
    clientes[login] = lista
def logar (geral:dict,vendedores:dict,clientes:dict):
    logado = False
    while not logado:

        print(53 * '=')
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')
        print(53 * '=')

        for cliente in geral.keys():
            if cliente == login:
                if (geral[login] == 'vendedor'):
                    for dados in vendedores.values():
                        if dados[4] == login:
                            if senha == dados[1]:
                                logado = True
                elif (geral[login] == 'cliente'):
                    for dados in clientes.values():
                        if dados[4] == login:
                            if senha == dados[1]:
                                logado = True
                    if not logado:
                        print('\033[0;30;41m Login ou senha incorretos. Digite novamente. \033[m')
        if not logado:
            print('\033[0;30;41m Login ou senha incorretos. Digite novamente. \033[m')
    dados_log = [login,senha,logado]
    return dados_log