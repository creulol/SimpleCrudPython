from time import sleep

opcoesMenu = ['Cadastrar Pessoa','Listar Pessoas','Remover Pessoa','Sair']
arq = 'pessoas.txt'

def arquivoExiste(nomeArq):
    try:
        a = open(nomeArq,'rt') # rt == Read Text ou seja abre e Lê o texto dentro
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criaArquivo(nomeArq):
    try:
        a = open(nomeArq,'wt+') # wt == Write Text ou seja escreve texto o + significa que se não existir o arquivo ele cria um novo
        a.close()
    except:
        print('Houve um erro na criacao do arquivo!!')
    else:
        print(f'\nArquivo {nomeArq} criado com sucesso!')

def lerArquivo(nomeArq):
    try:
        a = open(nomeArq,'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um ERRO na abertuda do Arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um ERRO na hora de gravar os dados!\033[m')
        else:
            print(f'Novo registro de {nome} cadastrado.')
            a.close()
            sleep(2)

def removeCadastro(arq, nome):
    if nome:
        with open(arq, "r") as f:
            lines = f.readlines()
            f.seek(0)
        with open(arq, "w") as f:
            for line in lines:
                if line.strip("\n") != nome:
                    if nome not in line:
                        f.write(line)
    else:
        print('\033[31mDigite um nome!!\033[m')
    print(f'Todos os registros com nome {nome} foram removidos com sucesso!')



def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido!.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mO usuário prefiriu não digitar o número.\033[m')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def montaCabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def montaOpc(opcs):
    c = 1
    for item in opcs:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())


def montaMenu():
    montaCabecalho('BEM VINDO AO SIMPLE CRUD')
    montaOpc(opcoesMenu)
    opc = leiaInt('Digite um número da opcão : ')
    logicaMenu(opc)
    return opc

def logicaMenu(opcao):
    qtdOpcoes = len(opcoesMenu)
    if opcao > 0 and opcao <= qtdOpcoes:
        if opcao == 1:
            montaCabecalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
            montaMenu()
        elif opcao == 2:
            montaCabecalho('PESSOAS CADASTRADAS')
            lerArquivo(arq)
            sleep(3)
            montaMenu()
        elif opcao == 3:
            montaCabecalho('REMOVER PESSOA')
            nome = str(input('Nome para remover: '))
            removeCadastro(arq, nome)
            montaMenu()
        else:
            print(f'\033[36mObrigado por utilizar o Simple Crud. Até a próxima...\033[m')
    else:
        print(f'\033[31mERRO: Digite um número válido entre 1 e {qtdOpcoes}.\033[m')
        sleep(2)
        montaMenu()
        
if arquivoExiste(arq):
    print(f'Arquivo {arq} encontrado com sucesso!')
else:
    print('\033[31mArquivo não encontrado! Gerando um novo\033[m',end='')
    sleep(0.5)
    print('. ', end='')
    sleep(0.5)
    print('. ', end='')
    sleep(0.5)
    print('. ', end='')
    criaArquivo(arq)

montaMenu()
