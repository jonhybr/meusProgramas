num = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        num += c
        print(c, end=' ')
print('\n', num)
