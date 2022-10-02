frase = str(input('Me diga uma frase e eu direi quantos "A" tem e onde aparece a primeira e a ultima vez:')).strip()
print(' A letra "A" apareceu: {} vezes\n apareceu primeiro na posição: {}\n apareceu por ultimo na posição: {}'
      .format(frase.upper().count('A'),frase.upper().find('A') + 1, frase.upper().rfind('A') + 1))
