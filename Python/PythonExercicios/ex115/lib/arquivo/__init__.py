from ex115.lib.interface import *

def existeArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo.')
    else:
        print(f'O arquivo {arquivo} foi criado com sucesso!')


def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        menu('Pessoas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Não foi possivel adicionar a pessoa.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao cadastrar a pessoa.')
        else:
            print('Pessoa cadastrada com sucesso.')
