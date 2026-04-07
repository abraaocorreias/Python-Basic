filmes = []
clientes = []
locacoes = []

while True:
    print('\nMENU PRINCIPAL\n')
    print('1 - Cadastrar filme')
    print('2 - Listar filmes')
    print('3 - Buscar filme')
    print('4 - Cadastrar cliente')
    print('5 - Listar clientes')
    print('6 - Buscar cliente (por id ou nome)')
    print('7 - Locar filme (criar locação)')
    print('8 - Devolver filme (finalizar locação)')
    print('9 - Listar locações')
    print('10 - Relatórios')
    print('11 - Salvar dados em TXT')
    print('12 - Carregar dados do TXT')
    print('0 - Sair')
    
    try:
        menu = int(input('\nDigite aqui o número da opção desejada: '))
    except ValueError:
        print('\n[ERRO] Por favor, digite apenas NÚMEROS (0 a 12).\n')
        continue
    
    if menu == 0:
        break
    elif menu == 1:
        print('\nVocê deseja cadastrar um filme.\n')
        titulo_cad = input('Digite aqui o título do filme: ')
        genero_cad = input('Digite aqui o gênero do filme: ')
        while True:
            try:
                ano_cad = int(input('Digite aqui o ano de lançamento do filme: '))
                break
            except ValueError:
                print('\n[ERRO] Por favor, digite um número válido para o ano.\n')
        disponibilidade_cad = True
        codigo_cad = len(filmes) + 1
        aluguel_cad = 0
        cadastro_filme = {
            'titulo': titulo_cad,
            'genero': genero_cad,
            'ano': ano_cad,
            'disponibilidade': disponibilidade_cad,
            'codigo': codigo_cad,
            'aluguel': aluguel_cad
        }
        filmes.append(cadastro_filme)
        
    elif menu == 2:
        #listar filmes, preciso verificar se a lista de filmes está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar os filmes cadastrados com suas informações.
        print('\nLista de filmes cadastrados:\n')
        for filme in filmes:
            print(f'Código: {filme["codigo"]} | Título: {filme["titulo"]} \nGênero: {filme["genero"]} \nAno: {filme["ano"]}')
            if filme['disponibilidade'] == True:
                print('Disponibilidade: Disponível\n')
            else:
                print('Disponibilidade: Indisponível\n')
            print(f'Filme foi alugado {filme["aluguel"]} vezes.\n')
                        
    elif menu == 3:
        #preciso por um if para verificar se a lista de filmes está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar o menu de busca e nesse menu de busca o usuário pode escolher se quer buscar por título ou por código depois mostrar os resultados da busca.
        print('\nVocê deseja buscar um filme.\n')
        busca_filme = input('Digite aqui o título do filme que deseja buscar: ')
        encontrado = False
        for filme in filmes:
            if filme['titulo'].lower() == busca_filme.lower():
                print(f'\nCódigo: {filme["codigo"]} | Título: {filme["titulo"]} \nGênero: {filme["genero"]} \nAno: {filme["ano"]}')
                if filme['disponibilidade'] == True:
                    print('Disponibilidade: Disponível\n')
                else:
                    print('Disponibilidade: Indisponível\n')
                print(f'Filme foi alugado {filme["aluguel"]} vezes.\n')
                encontrado = True
                break
        if not encontrado:
            print('\n[ERRO] Filme não encontrado. Verifique o título e tente novamente.\n')
        
    elif menu == 4:
        #Cadastrar cliente, preciso pedir o id, nome, telefone do cliente, locações ativas e o total de locações depois criar um dicionário com essas informações e adicionar esse dicionário a uma lista de clientes.
        cadastro_cliente = {
            'id_cliente': len(clientes) + 1,
            'nome': nome_cad,
            'telefone': telefone_cad,
            'locacoes_ativas': [],
            'total_locacoes': 0
        }
        clientes.append(cadastro_cliente)
    elif menu == 5:
        #listar clientes, preciso verificar se a lista de clientes está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar os clientes cadastrados com suas informações.
    elif menu == 6:
        #buscar cliente, preciso por um if para verificar se a lista de clientes está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar o menu de busca e nesse menu de busca o usuário pode escolher se quer buscar por id ou por nome depois mostrar os resultados da busca.
    elif menu == 7:
        #locar filme, preciso verificar se a lista de clientes e a lista de filmes estão vazias, caso estejam, mostrar uma mensagem de erro, caso contrário, pedir o id do cliente e o código do filme que deseja alugar depois verificar se o cliente existe e se o filme existe e se o filme está disponível, caso esteja disponível, criar um dicionário com as informações da locação (cliente, filme, data de locação e data de devolução) e adicionar esse dicionário a uma lista de locações e atualizar a disponibilidade do filme para False e adicionar o código do filme na lista de locações ativas do cliente e atualizar o total de locações do cliente.
    elif menu == 8:
        #devolver filme, preciso verificar se a lista de clientes e a lista de filmes estão vazias, caso estejam, mostrar uma mensagem de erro, caso contrário, pedir o id do cliente e o código do filme que deseja devolver depois verificar se o cliente existe e se o filme existe e se o filme está alugado para aquele cliente, caso esteja alugado para aquele cliente, atualizar a disponibilidade do filme para True e remover o código do filme da lista de locações ativas do cliente e atualizar o total de locações do cliente.
        
    elif menu == 9:
        #listar locações, preciso verificar se a lista de locações está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar as locações cadastradas com suas informações (cliente, filme, data de locação e data de devolução).
        
    elif menu == 10:
        #relatórios, preciso verificar se a lista de locações está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar um menu de relatórios onde o usuário pode escolher entre os seguintes relatórios: filmes mais alugados, clientes com mais locações, locações ativas e locações finalizadas.
        
    elif menu == 11:
        #salvar dados em txt, preciso criar um arquivo txt para cada lista (filmes, clientes e locações) e salvar os dados de cada lista nesse arquivo txt.
        
    elif menu == 12:
        #carregar dados do txt, preciso ler os arquivos txt criados no item 11 e carregar os dados de cada arquivo txt para as respectivas listas (filmes, clientes e locações).
        
    else:
        print('\n[ERRO] Opção inválida! Por favor, escolha um número entre 0 e 12.\n')

        
#tá zoado esse código abaixo
cadastro_locacao = {
    'id_': cliente_loc,
    'filme': filme_loc,
    'data_locacao': data_loc_cad,
    'data_devolucao': data_dev_cad
}
locacoes.append(cadastro_locacao)

