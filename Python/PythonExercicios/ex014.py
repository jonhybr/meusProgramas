graus: float = float(input('Quantos graus está fazendo aí?'))
fahrenheit = (graus * 9/5) + 32
print('Nossa {:.1f}°C aqui é {:.1f}°F que estranho'.format(graus,fahrenheit))