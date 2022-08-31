nome = str(input('Me diga o nome de uma cidade e eu direi se seu primeiro nome é Santo:'))
nomeS = nome.lower().split()
print('santo'in nomeS[0])