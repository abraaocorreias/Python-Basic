#Você vai criar um programa em Python que funciona como um mini sistema de cadastro de notas.
#O programa deve ter um menu que fica repetindo até o usuário escolher sair:
    #Menu
    #1 → Cadastrar aluno
    #2 → Listar alunos
        #3 → Mostrar relatório (média da turma, maior e menor média)
    #4 → Buscar aluno pelo nome
    #0 → Sair
#Cadastro de aluno (opção 1)
#Ao cadastrar, o programa deve pedir:
    #Nome do aluno
    #Nota 1 (0 a 10)
    #Nota 2 (0 a 10)
#E guardar em uma lista chamada alunos.


alunos  = []
sinal = False

soma_das_medias = 0
maior_media = 0
aluno_maior_media = ' '
menor_media = 11
aluno_menor_media = ' '

def calcular_media(a,b):
    return ((a+b)/2)





while True:
    print('MENU PRINCIPAL')
    print(' ')
    print('1  Cadastrar aluno(nome e notas);')
    print('2  Listar alunos cadastradas;')
    print('3  Mostrar relatório (média da turma, maior e menor média);')
    print('4  buscar aluno pelo nome;')
    print('0  Sair')

    try:
        menu = int(input('Digite aqui o número da opção desejada: '))
    except ValueError:
        print(' ')
        print("[ERRO] Por favor, digite apenas NÚMEROS (0, 1, 2, 3 ou 4).")
        print(' ')
        print(' ')
        print(' ')
        
        continue

    if menu == 0:
        break

    elif menu == 1:
        print('Você deseja cadastrar uma aluno.')
        nome_cad = input('Digite aqui o nome da aluno: ')
        nota_cad1 = float(input('Digite aqui a 1ª nota do aluno: '))
        while nota_cad1 < 0 or nota_cad1 > 10:
            print("Nota inválida! A nota deve estar entre 0 e 10.")
            nota_cad1 = float(input('Digite novamente a 1ª nota: '))
        nota_cad2 = float(input('Digite aqui a 2ª nota do aluno: '))
        while nota_cad2 < 0 or nota_cad2 > 10:
            print("Nota inválida! A nota deve estar entre 0 e 10.")
            nota_cad2 = float(input('Digite novamente a 2ª nota: '))
        
        cadastro = {
            'nome': nome_cad,
            'nota_1': nota_cad1,
            'nota_2': nota_cad2,
            'media_aluno': calcular_media(nota_cad1, nota_cad2)
        } 
        alunos.append(cadastro)
        soma_das_medias += cadastro['media_aluno']

        if cadastro['media_aluno'] < menor_media:
            menor_media = cadastro['media_aluno']
            aluno_menor_media = cadastro['nome']
        
        if cadastro['media_aluno'] > maior_media:
            maior_media = cadastro['media_aluno']
            aluno_maior_media = cadastro['nome']
        
    
    elif menu == 2:
        print('Você deseja a lista de alunos cadastradas.')
        print('Segue a lista')

        for aluno in alunos:
            print(f"Nome: {aluno['nome']} | Nota 1: {aluno['nota_1']} | Nota 2: {aluno['nota_2']} | Média: {aluno['media_aluno']:.2f}")
    
    elif menu == 3:
        num_alunos = len(alunos)
        if num_alunos > 1:
            media_total = soma_das_medias/num_alunos
            print(f'A turma possui {num_alunos} alunos.')
            print(f"Média da Turma: {media_total:.2f}")
            print(f'Maior média da turma: Aluno: {aluno_maior_media} | nota:{maior_media:.2f}')
            print(f'Menor média da turma: Aluno: {aluno_menor_media} | nota:{menor_media:.2f}')
        else:
            print ('É preciso cadastrar pelo menos dois alunos para gerar relatório')

    
    elif menu == 4:
        print('Você deseja encontrar alguma aluno cadastradas')
        nome_busca = input('Digite aqui o nome que deseja procurar: ')

        for aluno in alunos:
            if nome_busca.lower() == aluno['nome'].lower():
                print(f"Nome: {aluno['nome']} | Nota 1: {aluno['nota_1']} | Nota 2: {aluno['nota_2']} | Média: {aluno['media_aluno']:.2f}")
                sinal = True
                break

        if sinal == False:
            print('aluno não encontrada')
        
    else:
        print('Opção inválida')
        print('Tente novamente')
    
    sinal = False

print('Menu Encerrado')
