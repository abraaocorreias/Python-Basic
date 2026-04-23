# Projeto Final: Python - Conceitos Básicos 
# OXETECH - Prof. Pedro Pires
# Aluno: Abraão Correia dos Santos


# Objetivo do Projeto: Você deverá desenvolver, em Python, um sistema de locadora de filmes que funcione pelo terminal (console). O sistema deve permitir cadastrar filmes e clientes, realizar locações e devoluções, gerar relatórios, e salvar/carregar os dados utilizando arquivos .txt.
# Regras Gerais do Projeto
    # O programa deve funcionar em loop com while, exibindo um menu até o usuário escolher sair.
    # Use listas para armazenar os registros.
    # Cada registro (filme, cliente, locação) deve ser representado por um dicionário.
    # O código deve usar funções para organizar cada ação do menu (ex: cadastrar filme, listar clientes, etc.).
    # Deve haver pelo menos um ponto do sistema usando try/except para evitar travamentos (por exemplo, ao ler números).
# Estruturas que Devem Existir
    # 1. Filmes (lista de dicionários) Cada filme deve conter:
        # codigo (número único)
        # titulo (texto)
        # ano (número)
        # disponivel (True/False)
        # alugueis (quantas vezes foi alugado)
    # 2. Clientes (lista de dicionários) Cada cliente deve conter:
        # id (número único)
        # nome
        # telefone
        # locacoes_ativas (quantas locações em aberto)
        # total_locacoes (quantas locações já fez)
    # 3. Locações (lista de dicionários) Cada locação deve conter:
        # id (número único)
        # cliente_id
        # filme_codigo
        # status (ATIVA ou FINALIZADA)
# Funcionalidades Obrigatórias (Menu) O programa deve exibir um menu com as opções abaixo:
    # Cadastrar filme
    # Listar filmes
    # Buscar filme (por código ou título)
    # Cadastrar cliente
    # Listar clientes
    # Buscar cliente (por id ou nome)
    # Locar filme (criar locação)
    # Devolver filme (finalizar locação)
    # Listar locações
    # Relatórios
    # Sair

# Json é uma biblioteca do Python que permite trabalhar com dados em formato JSON (JavaScript Object Notation). Ela é útil para salvar e carregar os dados do sistema de locadora em arquivos .txt, permitindo que os dados sejam armazenados de forma estruturada e fácil de ler. Com a função json.dump(), podemos salvar os dados em formato JSON dentro dos arquivos .txt, e com a função json.load(), podemos ler os dados em formato JSON dos arquivos .txt e carregar esses dados para as listas correspondentes no programa.
import json

#listas para armazenar os registros de filmes, clientes e locações

filmes = []
clientes = []
locacoes = []

def verificar_lista_vazia(lista, tipo):
    #função para verificar se a lista de filmes, clientes ou locações está vazia, caso esteja, mostrar uma mensagem de erro e retornar True, caso contrário, retornar False.
    if not lista:
        print(f'\n[ERRO] A lista de {tipo} está vazia! Por favor, cadastre {tipo} antes de realizar esta ação.\n')
        return True
    return False

def cadastrar_filme(filmes):
    #Cadastrar filme, preciso pedir o código, título, gênero, ano de lançamento e disponibilidade do filme depois criar um dicionário com essas informações e adicionar esse dicionário a uma lista de filmes.
    titulo_cad = input('Digite aqui o título do filme: ')
    ano_filme_cad = input('Digite aqui o ano de lançamento do filme: ')
    genero_cad = input('Digite aqui o gênero do filme: ')
    disponibilidade_cad = True
    codigo_cad = len(filmes) + 1
    aluguel_cad = 0
    cadastro_filme = {
        'titulo': titulo_cad,
        'ano': ano_filme_cad,
        'genero': genero_cad,
        'disponibilidade': disponibilidade_cad,
        'codigo': codigo_cad,
        'aluguel': aluguel_cad
    }
    filmes.append(cadastro_filme)

def listar_filmes(filmes):
    #listar filmes, preciso verificar se a lista de filmes está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar os filmes cadastrados com suas informações.
    if verificar_lista_vazia(filmes, "filmes"):
        return
    print('\nLista de filmes cadastrados:\n')
    for filme in filmes:
        print(f'Código: {filme["codigo"]} \nTítulo: {filme["titulo"]} \nGênero: {filme["genero"]} \nAno: {filme["ano"]}')
        if filme['disponibilidade'] == True:
            print('Disponibilidade: Disponível\n')
        else:
            print('Disponibilidade: Indisponível\n')
        print(f'Filme foi alugado {filme["aluguel"]} vezes.\n')

def buscar_filme(filmes):
    #preciso por um if para verificar se a lista de filmes está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar o menu de busca e nesse menu de busca o usuário pode escolher se quer buscar por título ou por código depois mostrar os resultados da busca.
    if verificar_lista_vazia(filmes, "filmes"):
        return
    
    print('\n--- Buscar Filme ---')
    print('1 - Buscar por Título')
    print('2 - Buscar por Código')
    
    escolha = input('Escolha uma opção (1 ou 2): ')
    encontrado = False
    
    if escolha == '1':
        busca_titulo = input('Digite o título: ').lower()
        for filme in filmes:
            if filme['titulo'].lower() == busca_titulo:
                print(f'\nCódigo: {filme["codigo"]} \nTítulo: {filme["titulo"]} \nGênero: {filme["genero"]} \nAno: {filme["ano"]}')
                if filme['disponibilidade'] == True:
                    print('Disponibilidade: Disponível\n')
                else:
                    print('Disponibilidade: Indisponível\n')
                print(f'Filme foi alugado {filme["aluguel"]} vezes.\n')
                encontrado = True
                break
    elif escolha == '2':
        try:
            busca_codigo = int(input('Digite o código: '))
        except ValueError:
            print('\n[ERRO] Por favor, digite um número válido para o código do filme.\n')
            return
        for filme in filmes:
            if filme['codigo'] == busca_codigo:
                print(f'\nCódigo: {filme["codigo"]} \nTítulo: {filme["titulo"]} \nGênero: {filme["genero"]} \nAno: {filme["ano"]}')
                if filme['disponibilidade'] == True:
                    print('Disponibilidade: Disponível\n')
                else:
                    print('Disponibilidade: Indisponível\n')
                print(f'Filme foi alugado {filme["aluguel"]} vezes.\n')
                encontrado = True
                break        
    else:
        print('\n[ERRO] Opção de busca inválida.\n')

def cadastrar_cliente(clientes):
    #Cadastrar cliente, preciso pedir o id, nome, telefone do cliente, locações ativas e o total de locações depois criar um dicionário com essas informações e adicionar esse dicionário a uma lista de clientes.
    nome_cad = input('Digite aqui o nome do cliente: ')
    telefone_cad = input('Digite aqui o telefone do cliente: ')
    cadastro_cliente = {
            'id_cliente': len(clientes) + 1,
            'nome': nome_cad,
            'telefone': telefone_cad,
            'locacoes_ativas': 0,
            'total_locacoes': 0
        }
    clientes.append(cadastro_cliente)

def listar_clientes(clientes):
    #listar clientes, preciso verificar se a lista de clientes está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar os clientes cadastrados com suas informações.
    if verificar_lista_vazia(clientes, "clientes"):
        return
    print('\nLista de clientes cadastrados:\n')
    for cliente in clientes:
        print(f'ID: {cliente["id_cliente"]} \nNome: {cliente["nome"]} \nTelefone: {cliente["telefone"]} \nLocações ativas: {cliente["locacoes_ativas"]} \nTotal de locações: {cliente["total_locacoes"]}\n\n')

def buscar_cliente(clientes):
    #buscar cliente, preciso por um if para verificar se a lista de clientes está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar o menu de busca e nesse menu de busca o usuário pode escolher se quer buscar por id ou por nome depois mostrar os resultados da busca.
    if verificar_lista_vazia(clientes, "clientes"):
        return
    print('\nVocê deseja buscar um cliente.\n')
    print('1 - Buscar por ID')
    print('2 - Buscar por Nome')
    escolha = input('Escolha uma opção (1 ou 2): ')

    if escolha == '1':
        try:
            buscar_cliente_id = int(input('Digite aqui o ID do cliente que deseja buscar: '))
        except ValueError:
            print('\n[ERRO] Por favor, digite um número válido para o ID do cliente.\n')
            return
        encontrado = False
        for cliente in clientes:
            if cliente['id_cliente'] == buscar_cliente_id:
                print(f'\nID: {cliente["id_cliente"]} \nNome: {cliente["nome"]} \nTelefone: {cliente["telefone"]} \nLocações ativas: {cliente["locacoes_ativas"]} \nTotal de locações: {cliente["total_locacoes"]}\n\n')
                encontrado = True
                break
        if not encontrado:
            print('\n[ERRO] Cliente não encontrado. Verifique o ID e tente novamente.\n')
    elif escolha == '2':
        buscar_cliente_nome = input('Digite aqui o nome do cliente que deseja buscar: ')
        encontrado = False
        for cliente in clientes:
            if cliente['nome'].lower() == buscar_cliente_nome.lower():
                print(f'\nID: {cliente["id_cliente"]} \nNome: {cliente["nome"]} \nTelefone: {cliente["telefone"]} \nLocações ativas: {cliente["locacoes_ativas"]} \nTotal de locações: {cliente["total_locacoes"]}\n\n')
                encontrado = True
                break
        if not encontrado:
            print('\n[ERRO] Cliente não encontrado. Verifique o nome e tente novamente.\n')


def locar_filme(clientes, filmes, locacoes):
    #locar filme, preciso verificar se a lista de clientes e a lista de filmes estão vazias, caso estejam, mostrar uma mensagem de erro, caso contrário, pedir o id do cliente e o código do filme que deseja alugar depois verificar se o client existe e se o filme existe e se o filme está disponível, caso esteja disponível, criar um dicionário com as informações da locação (cliente, filme, data de locação e data de devolução) e adicionar esse dicionário a uma lista de locações e atualizar a disponibilidade do filme para False e adicionar o código do filme na lista de locações ativas do cliente e atualizar o total de locações do cliente.
    if verificar_lista_vazia(clientes, "clientes") or verificar_lista_vazia(filmes, "filmes"):
        return
    
    try:
        id_cliente = int(input('Digite o ID do cliente que deseja locar um filme: '))
    except ValueError:
        print('\n[ERRO] Por favor, digite um número válido para o ID do cliente.\n')
        return
    
    try:
        codigo_filme = int(input('Digite o código do filme que deseja locar: '))
    except ValueError:
        print('\n[ERRO] Por favor, digite um número válido para o código do filme.\n')
        return
    
    cliente_encontrado = None
    for cliente in clientes:
        if cliente['id_cliente'] == id_cliente:
            cliente_encontrado = cliente
            break
    
    if not cliente_encontrado:
        print('\n[ERRO] Cliente não encontrado. Verifique o ID e tente novamente.\n')
        return
    
    filme_encontrado = None
    for filme in filmes:
        if filme['codigo'] == codigo_filme:
            filme_encontrado = filme
            break
    
    if not filme_encontrado:
        print('\n[ERRO] Filme não encontrado. Verifique o código e tente novamente.\n')
        return
    
    if not filme_encontrado['disponibilidade']:
        print('\n[ERRO] Filme indisponível para locação. Escolha outro filme ou aguarde a devolução.\n')
        return
    
    # Criar a locação
    nova_locacao = {
        'id_locacao': len(locacoes) + 1,
        'cliente_id': id_cliente,
        'filme_codigo': codigo_filme,
        'status': 'ATIVA'
    }
    
    locacoes.append(nova_locacao)
    
    # Atualizar disponibilidade do filme e informações do cliente
    filme_encontrado['disponibilidade'] = False
    filme_encontrado['aluguel'] += 1
    cliente_encontrado['locacoes_ativas'] += 1
    cliente_encontrado['total_locacoes'] += 1
    
    print(f'\nLocação realizada com sucesso! O cliente "{cliente_encontrado["nome"]}" alugou o filme "{filme_encontrado["titulo"]}".\n')
    

def devolver_filme(clientes, filmes, locacoes):
    #devolver filme, preciso verificar se a lista de clientes e a lista de filmes estão vazias, caso estejam, mostrar uma mensagem de erro, caso contrário, pedir o id do cliente e o código do filme que deseja devolver depois verificar se o cliente existe e se o filme existe e se o filme está alugado para aquele cliente, caso esteja alugado para aquele cliente, atualizar a disponibilidade do filme para True e remover o código do filme da lista de locações ativas do cliente e atualizar o total de locações do cliente.

    if verificar_lista_vazia(clientes, "clientes") or verificar_lista_vazia(filmes, "filmes") or verificar_lista_vazia(locacoes, "locações"):
        return
    
    try:
        id_cliente = int(input('Digite o ID do cliente que deseja devolver um filme: '))
    except ValueError:
        print('\n[ERRO] Por favor, digite um número válido para o ID do cliente.\n')
        return
    
    try:
        codigo_filme = int(input('Digite o código do filme que deseja devolver: '))
    except ValueError:
        print('\n[ERRO] Por favor, digite um número válido para o código do filme.\n')
        return
    
    cliente_encontrado = None
    for cliente in clientes:
        if cliente['id_cliente'] == id_cliente:
            cliente_encontrado = cliente
            break
    
    if not cliente_encontrado:
        print('\n[ERRO] Cliente não encontrado. Verifique o ID e tente novamente.\n')
        return
    
    filme_encontrado = None
    for filme in filmes:
        if filme['codigo'] == codigo_filme:
            filme_encontrado = filme
            break
    
    if not filme_encontrado:
        print('\n[ERRO] Filme não encontrado. Verifique o código e tente novamente.\n')
        return
    
    locacao_encontrada = None
    for locacao in locacoes:
        if locacao['cliente_id'] == id_cliente and locacao['filme_codigo'] == codigo_filme and locacao['status'] == 'ATIVA':
            locacao_encontrada = locacao
            break
    
    if not locacao_encontrada:
        print('\n[ERRO] Locação ativa não encontrada para este cliente e filme. Verifique as informações e tente novamente.\n')
        return
    
    # Finalizar a locação
    locacao_encontrada['status'] = 'FINALIZADA'
    
    # Atualizar disponibilidade do filme e informações do cliente
    filme_encontrado['disponibilidade'] = True
    cliente_encontrado['locacoes_ativas'] -= 1
    
    print(f'\nDevolução realizada com sucesso! O cliente "{cliente_encontrado["nome"]}" devolveu o filme "{filme_encontrado["titulo"]}".\n')

def listar_locacoes(locacoes):
    #listar locações, preciso verificar se a lista de locações está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar as locações cadastradas com suas informações (cliente, filme, data de locação e data de devolução).
    if verificar_lista_vazia(locacoes, "locações"):
        return
    print('\nLista de locações:\n')
    for locacao in locacoes:
        print(f'ID da Locação: {locacao["id_locacao"]} \nID do Cliente: {locacao["cliente_id"]} \nCódigo do Filme: {locacao["filme_codigo"]} \nStatus: {locacao["status"]}\n\n')

def gerar_relatorios(locacoes, clientes, filmes):
    #relatórios, preciso verificar se a lista de locações está vazia, caso esteja, mostrar uma mensagem de erro, caso contrário, mostrar um menu de relatórios onde o usuário pode escolher entre os seguintes relatórios: filmes mais alugados, clientes com mais locações, locações ativas e locações finalizadas. Cada relatório deve mostrar as informações relevantes de acordo com o tipo de relatório escolhido. Por exemplo, o relatório de filmes mais alugados deve mostrar o título do filme e a quantidade de vezes que ele foi alugado, o relatório de clientes com mais locações deve mostrar o nome do cliente e a quantidade total de locações que ele fez, o relatório de locações ativas deve mostrar o ID da locação, o nome do cliente e o título do filme para cada locação que ainda está ativa, e o relatório de locações finalizadas deve mostrar o ID da locação, o nome do cliente e o título do filme para cada locação que já foi finalizada.
    if verificar_lista_vazia(locacoes, "locações"):
        return
    
    print('\n--- Relatórios ---')
    
    # 1. Encontrar o filme mais alugado
    maior_aluguel = -1
    filme_campeao = ""
    
    for filme in filmes:
        if filme['aluguel'] > maior_aluguel:
            maior_aluguel = filme['aluguel']
            filme_campeao = filme['titulo']
            
    if maior_aluguel > 0:
        print(f'\n-> Filme mais alugado: {filme_campeao} (Alugado {maior_aluguel} vezes)')
    else:
        print('\n-> Nenhum filme foi alugado ainda.')

    # 2. Encontrar o cliente com mais locações
    maior_total_locacoes = -1
    cliente_campeao = ""
    
    for cliente in clientes:
        if cliente['total_locacoes'] > maior_total_locacoes:
            maior_total_locacoes = cliente['total_locacoes']
            cliente_campeao = cliente['nome']
            
    if maior_total_locacoes > 0:
        print(f'-> Cliente com mais locações: {cliente_campeao} (Total de {maior_total_locacoes} locações)')

    # 3. Listar Locações Ativas 
    print('\n--- Locações Ativas ---')
    achou_ativa = False
    
    for locacao in locacoes:
        if locacao['status'] == 'ATIVA':
            achou_ativa = True
            
            nome_cliente = "Desconhecido"
            for c in clientes:
                if c['id_cliente'] == locacao['cliente_id']:
                    nome_cliente = c['nome']
                    break
                    
            titulo_filme = "Desconhecido"
            for f in filmes:
                if f['codigo'] == locacao['filme_codigo']:
                    titulo_filme = f['titulo']
                    break
                    
            print(f'ID Locação: {locacao["id_locacao"]} | Cliente: {nome_cliente} | Filme: {titulo_filme}')
            
    if not achou_ativa:
        print('Nenhuma locação ativa no momento.')

    # 4. Listar Locações Finalizadas
    print('\n--- Locações Finalizadas ---')
    achou_finalizada = False
    
    for locacao in locacoes:
        if locacao['status'] == 'FINALIZADA':
            achou_finalizada = True
            
            nome_cliente = "Desconhecido"
            for c in clientes:
                if c['id_cliente'] == locacao['cliente_id']:
                    nome_cliente = c['nome']
                    break
                    
            titulo_filme = "Desconhecido"
            for f in filmes:
                if f['codigo'] == locacao['filme_codigo']:
                    titulo_filme = f['titulo']
                    break
                    
            print(f'ID Locação: {locacao["id_locacao"]} | Cliente: {nome_cliente} | Filme: {titulo_filme}')
            
    if not achou_finalizada:
        print('Nenhuma locação finalizada no momento.\n')
    
def salvar_dados(filmes, clientes, locacoes):
    #salvar dados em txt, preciso criar um arquivo txt para cada lista (filmes, clientes e locações) e salvar os dados de cada lista nesse arquivo txt. Para isso, vou usar a função json.dump() para salvar os dados em formato JSON dentro dos arquivos txt.
    with open('filmes.txt', 'w') as arquivo_filmes:
        json.dump(filmes, arquivo_filmes)
        
    with open('clientes.txt', 'w') as arquivo_clientes:
        json.dump(clientes, arquivo_clientes)
        
    with open('locacoes.txt', 'w') as arquivo_locacoes:
        json.dump(locacoes, arquivo_locacoes)
        
    print('\n[SUCESSO] Todos os dados foram salvos com sucesso nos arquivos TXT!\n')

def carregar_dados(filmes, clientes, locacoes):
    #carregar dados do txt, preciso ler os arquivos txt criados no item 11 e carregar os dados de cada arquivo txt para as respectivas listas (filmes, clientes e locações). Para isso, vou usar a função json.load() para ler os dados em formato JSON dos arquivos txt e carregar esses dados para as listas correspondentes. Vou usar um bloco try/except para tratar o caso em que os arquivos txt não existam ou estejam vazios, mostrando uma mensagem de erro caso isso aconteça.
    try:
        with open('filmes.txt', 'r') as arquivo_filmes:
            filmes.clear()
            filmes.extend(json.load(arquivo_filmes))
            
        with open('clientes.txt', 'r') as arquivo_clientes:
            clientes.clear()
            clientes.extend(json.load(arquivo_clientes))
            
        with open('locacoes.txt', 'r') as arquivo_locacoes:
            locacoes.clear()
            locacoes.extend(json.load(arquivo_locacoes))
            
        print('\n[SUCESSO] Dados carregados com sucesso dos arquivos TXT!\n')
        
    except FileNotFoundError:
        print('\n[ERRO] Nenhum arquivo de salvamento encontrado. Salve os dados primeiro.\n')


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
        cadastrar_filme(filmes)
        
    
    elif menu == 2:
        listar_filmes(filmes)
                        
    elif menu == 3:
        buscar_filme(filmes)
        
        
    elif menu == 4:
        cadastrar_cliente(clientes)

    elif menu == 5:
        listar_clientes(clientes)

    elif menu == 6:
        buscar_cliente(clientes)

    elif menu == 7:
        locar_filme(clientes, filmes, locacoes)

    elif menu == 8:
        devolver_filme(clientes, filmes, locacoes)

    elif menu == 9:
        listar_locacoes(locacoes)

        
    elif menu == 10:
        gerar_relatorios(locacoes, clientes, filmes)
        
    elif menu == 11:
        salvar_dados(filmes, clientes, locacoes)

        
    elif menu == 12:
        carregar_dados(filmes, clientes, locacoes)
        
    else:
        print('\n[ERRO] Opção inválida! Por favor, escolha um número entre 0 e 12.\n')