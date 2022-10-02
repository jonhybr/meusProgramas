def notas(* nots, sit=False):
    disc = {'Notas': len(nots), 'Maior': 0, 'Menor': 10, 'Media': 0}
    media = 0
    for nota in nots:
        if nota > disc['Maior']:
            disc['Maior'] = nota
        if nota < disc['Menor']:
            disc['Menor'] = nota
        media += nota
    media = media / len(nots)
    disc['Media'] = media
    if sit:
        if media < 5:
            disc['Situação'] = 'Ruim'
        elif media < 7:
            disc['Situação'] = 'Ok'
        else:
            disc['Situação'] = 'Ótima'
    return disc


resul = notas(2, 4, 5, 6, sit=True)
print(resul)
