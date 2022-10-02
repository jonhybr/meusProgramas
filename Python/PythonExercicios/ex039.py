from datetime import date
nasc = int(input('Em que ano você nasceu?'))
anoA = date.today().year
idade = anoA - nasc
menor = (anoA - nasc - 18) *-1
maior = (anoA - nasc - 18)

if idade < 18:
    print('Você terá que ir para o exército no ano de {}, daqui {} ano(s)'.format(nasc + 18, menor))
elif idade > 18:
    print('Se você ainda não se alistou no exército, você deveria ter ido a {} ano(s), no ano de {}'.format(maior, nasc + 18))
elif idade == 18:
    print('Você precisa se alistar agora no ano de {}!'.format(anoA))
