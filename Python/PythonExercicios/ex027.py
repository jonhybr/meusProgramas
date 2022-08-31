nome = str(input('Olá, diga-me seu nome:')).title()
nomeS = nome.split()
print(' Bem-vindo(a) {}\n Seu primeiro nome é: {}\n Seu ultimo nome é: {}'.format(nome,nomeS[0], nomeS[len(nomeS)-1]))