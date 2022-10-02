jogos = 'Super Mario Galaxy 2', 'The Legend of Zelda: Breath of the Wild', 'Red Dead Redemption 2',\
        'Grand Theft Auto V', 'Super Mario Odyssey', 'Mass Effect 2', 'The Elder Scrolls V: Skyrim', 'The Last of Us',\
        'Red Dead Redemption', 'Portal 2', 'God of War', 'Batman: Arkham City',\
        'The Legend of Zelda: Ocarina of Time 3D', 'BioShock Infinite', 'Pac-Man Championship Edition DX',\
        'Divinity: Original Sin II', 'Super Mario 3D World', 'StarCraft II: Wings of Liberty', 'Minecraft',\
        'Persona 4 Golden'

print('Os 20 jogos mais bem avaliados no metacritics são: ', end='')
for j in jogos:
    print(j, end=', ')
print('\nOs 5 jogos com maiores notas no metacritics são: ', end='')
for j in jogos[0:5]:
    print(j, end=', ')
print('\nOs 4 jogos com menos notas no metacritics são: ', end='')
for j in jogos[-4:]:
    print(j, end=', ')
print('\nOs jogos em ordem alfabética: ', sorted(jogos))
print(f'O jogo GTA V se encontra na {jogos.index("Grand Theft Auto V") + 1} posição')