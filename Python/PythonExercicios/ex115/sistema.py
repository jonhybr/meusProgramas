from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'pessoas.txt'

if not existeArquivo(arq):
    criarArquivo(arq)

while True:
    resposta = opcoes(['Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        menu('Cadastrar')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        break
    else:
        print('Erro! Digite uma opção valida.')

