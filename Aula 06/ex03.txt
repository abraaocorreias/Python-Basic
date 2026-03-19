#Crie um programa que tenha um menu repetindo:
    #1  Cadastrar pessoa(nome e idade);
    #2  Listar pessoas cadastradas;
    #3  buscar pessoa pelo nome;
    #0  Sair
#Regras:
    #   Guarde as pessoas em uma lista chamada pessoas;
    #   Cada pessoa deve ser um dicionério com "nome" e "Idade";
    #   Na busca, se enccontrar, mostre os dados. Se não encontrar, mostre "Pessoa não encontrada".

pessoa1 = {
    'nome': 'Abraão',
    'idade': 29
}

pessoas  = [pessoa1]
sinal = False


print('MENU PRINCIPAL')
print(' ')
print('1  Cadastrar pessoa(nome e idade);')
print('2  Listar pessoas cadastradas;')
print('3  buscar pessoa pelo nome;')
print('0  Sair')

menu = int(input('Digite aqui o número da opção desejada: '))

while menu != 0:

    if menu == 1:
        print('Você deseja cadastrar uma pessoa.')
        nome_cad = input('Digite aqui o nome da pessoa: ')
        idade_cad = int(input('Digite aqui a idade da pesssoa: '))
        cadastro = {
            'nome': nome_cad,
            'idade': idade_cad
        } 
        pessoas.append(cadastro)
    
    elif menu == 2:
        print('Você deseja a lista de pessoas cadastradas.')
        print('Segue a lista')

        for pessoa in pessoas:
            print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']} anos")
    
    elif menu == 3:
        print('Você deseja encontrar alguma pessoa cadastradas')
        nome_busca = input('Digite aqui o nome que deseja procurar: ')

        for pessoa in pessoas:
            if nome_busca.lower() == pessoa['nome'].lower():
                print(f"Nome: {pessoa['nome']} | Idade: {pessoa['idade']} anos")
                sinal = True
                break

        if sinal == False:
            print('Pessoa não encontrada')
        
    else:
        print('Opção inválida')
        print('Tente novamente')
    
    sinal = False
    print('MENU PRINCIPAL')
    print(' ')
    print('1  Cadastrar pessoa(nome e idade);')
    print('2  Listar pessoas cadastradas;')
    print('3  buscar pessoa pelo nome;')
    print('0  Sair')

    menu = int(input('Digite aqui a opção desejada: '))

print('Menu Encerrado')
