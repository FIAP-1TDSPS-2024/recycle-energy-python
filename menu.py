import os
import platform

# Seleciona o comando de limpar a tela de acordo com o sistema operacional
clearCommand = 'cls'
if platform.system() == 'Linux' or platform.system() == 'Darwin':
    clearCommand = 'clear'


# Função para a área do funcionário
def login():
    emailCorreto = "teste@gmail.com"
    senhaCorreta = "1234"

    while True:
        os.system(clearCommand)
        print('Você escolheu a opção de login!')

        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')

        if email == emailCorreto and senha == senhaCorreta:
            print('Login efetuado com sucesso!')
        else:
            print('Email ou senha inválidos!')

        opcao = input('Deseja tentar novamente? (s/n): ')
        if opcao == 'n':
            break

def cadastro():
    os.system(clearCommand)

    while True:
        print('Você escolheu a opção de cadastro!')

        dadosCadastro = {}

        dadosCadastro['nome'] = input('Digite seu nome: ')
        dadosCadastro['email'] = input('Digite seu email: ')
        dadosCadastro['senha'] = input('Digite sua senha: ')
        dadosCadastro['telefone'] = input('Digite seu telefone: ')

        print(f'Cadastro efetuado com sucesso! \n Bem-vindo(a) {dadosCadastro["nome"]}!')

        opcao = input('Deseja cadastrar outra pessoa? (s/n): ')
        if opcao == 'n':
            break

def calcular_preco_energia(): 
    os.system(clearCommand)
    print('Você escolheu a opção de calcular preço da energia!')

    while True:
        kwh = float(input('Digite a quantidade de kwh consumida: '))
        preco = 0.60

        print(f'O valor a ser pago é de R$ {kwh * preco}')

        opcao = input('Deseja calcular o preço de outra quantidade de kwh? (s/n): ')
        if opcao == 'n':
            break
        

# Função para a área do cliente
def area_cliente():
    while True:
        os.system(clearCommand)

        print('===== Área do cliente =====')
        print('Você entrou na área do cliente!')

        print('Escolha uma das opções abaixo:')
        print('1 - Login')
        print('2 - Cadastro')
        print('3 - Calcular preço da energia')
        print('4 - Voltar')

        # Ler opção do usuário
        opcao = input('Digite o número da opção escolhida: ')

        # Redireciona para a função escolhida
        if opcao == '1':
            login()
        elif opcao == '2':
            cadastro()
        elif opcao == '3':
            calcular_preco_energia()
        elif opcao == '4':
            break
        else:
            os.system(clearCommand)
            print('Opção inválida, favor tente novamente!')

# Função para o relatório de energia gerada
def relatorio_energia():
    os.system(clearCommand)
    print('Você escolheu a opção de relatório de energia gerada!')

    fontes_energia = ['Papel', 'Plástico', 'Vidro', 'Metal', 'Orgânico']
    energia_gerada = [100, 200, 300, 400, 500]

    for i in range(len(fontes_energia)):
        print(f'{fontes_energia[i]} gerou {energia_gerada[i]} kwh')

    input('Pressione enter para voltar ao menu...')
   
   
def area_funcionario():
    while True:
        os.system(clearCommand)

        print('===== Área do funcionário =====')
        print('Você entrou na área do funcionário!')

        print('Escolha uma das opções abaixo:')
        print('1 - Relatório de energia gerada')
        print('2 - Cadastro de cliente')
        print('3 - Voltar')

        # Ler opção do usuário
        opcao = input('Digite o número da opção escolhida: ')

        # Redireciona para a função escolhida
        if opcao == '1':
            relatorio_energia()
        elif opcao == '2':
            cadastro()
        elif opcao == '3':
            break
        else:
            os.system(clearCommand)
            print('Opção inválida, favor tente novamente!')

# Função para sair do programa
def sair():
    os.system(clearCommand)  
    print('Você optou por sair do app. Obrigado por utilizar o CaTech!')

# Função principal que exibe o menu 
def menu_principal():
    while True:
        os.system(clearCommand)
        print('Seja bem-vindo ao menu do Recycle Energy!')
        print('Escolha uma das opções abaixo:')
        print('1 - Área do cliente')
        print('2 - Área funcionario')
        print('3 - Sair')
        
        # Ler opção do usuário
        opcao = input('Digite o número da opção escolhida: ')

        # Redireciona para a função escolhida
        if opcao == '1':
            area_cliente()
        elif opcao == '2':
            area_funcionario()
        elif opcao == '3':
            sair()
            break  # Sai do programa
        else:
            os.system(clearCommand)
            print('Opção inválida, favor tente novamente!')


# Executa o menu principal
menu_principal()