import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo': False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    print ('''
╭━━━━╮╱╱╭╮╱╱╱╱╭╮╱╱╱╱╱╱╱//╭╮╱╱╱╱╱╱╱╱╱╱╱╭╮/////////////
┃╭╮╭╮┃╱╱┃┃╱╱╱╭╯╰╮╱╱╱╱╱╱//┃┃╱╱╱╱╱╱╱╱╱╱╱┃┃////////////
╰╯┃┃┣╋━╮┃┃╭┳━┻╮╭╋━━┳━╮╱//┃┃╱╱╭╮╭┳━╮╭━━┫╰━┳┳━━┳━━╮//
╱╱┃┃┣┫╭╮┫╰╯┫╭╮┃┃┃╭╮┃╭╮╮//┃┃╱╭┫┃┃┃╭╮┫╭━┫╭╮┣┫┃━┫━━┫//
╱╱┃┃┃┃┃┃┃╭╮┫╭╮┃╰┫╰╯┃┃┃┃//┃╰━╯┃╰╯┃┃┃┃╰━┫┃┃┃┃┃━╋━━┃//
╱╱╰╯╰┻╯╰┻╯╰┻╯╰┻━┻━━┻╯╰╯//╰━━━┻━━┻╯╰┻━━┻╯╰┻┻━━┻━━╯//

''')

def exibir_opcoes():
    print ('1. Cadastrar restaurante')
    print ('2. Listar restaurantes')
    print ('3. Alternar estado do restaurante')
    print ('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('\nFinalizando o app.\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    os.system('cls')
    print('\nOpção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def cadastrar_novo_restaurante():
    exibir_subtitulo('\nCadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('\nListando os restaurantes\n')

    print(f'{'Nome do Restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma Opção: ')) # Também posso transformar a string em INT depois de um momento específico com: opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()