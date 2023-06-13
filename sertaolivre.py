# Samuel Dantas de Albuquerque;
# Yan Kennedy Dantas Egídio.

import menu_site
import menu_cliente
import menu_vendedores

vendedores = {}
produtos = {}
clientes = {}
geral = {}
compras = {}

while True:
    logado = False
    opcao = menu_site.menu()
    if (opcao == '0'):
        break
    elif (opcao == '1'):
        menu_site.cadastrar_vendedores(geral,vendedores,clientes)
    elif (opcao == '2'):
        menu_site.cadastrar_cliente(geral,clientes,vendedores)
    elif (opcao == '3'):
        dados_log = menu_site.logar(geral,vendedores,clientes)
        login = dados_log[0]
        senha = dados_log[1]
        logado = dados_log[2]
        if(geral[login] == 'vendedor'):
            while (logado == True):
                opcao = menu_vendedores.menu()

                if (opcao == '0'):
                    break
                elif opcao == '1':
                    menu_vendedores.alterar_dados(login,vendedores)
                elif (opcao == '2'):
                    menu_vendedores.cadastrar_produto(login, produtos)
                elif (opcao == '3'):
                    menu_vendedores.buscar_produtos(login,produtos)
                elif (opcao == '4'):
                    menu_vendedores.remover_produto(login,produtos)
                elif opcao == '5':
                    menu_vendedores.atualizar_produto(login,produtos)
                elif opcao == '6':
                    menu_vendedores.gerar_grafico(login,produtos)
                elif opcao == '7':
                    menu_vendedores.salvarprodutos(login,produtos)
                else:
                    print('Opcao invalida')
        else:
            while True:
                opcao = menu_cliente.menu()
                if opcao == '0':
                    break
                elif(opcao == '1'):
                    menu_cliente.alterar_dados(login, clientes)
                elif(opcao == '2'):
                    menu_cliente.buscar_produto(login,produtos,compras)
                elif(opcao == '3'):
                    menu_cliente.compras_feitas(login,compras)
                elif(opcao == '4'):
                    menu_cliente.gpt_consulta(produtos)
                else:
                    print('Opcao Invalida')
    else:
        print('Opcao invalida')