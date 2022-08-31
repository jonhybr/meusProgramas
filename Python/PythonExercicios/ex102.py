def fatorial(num, show=False):
    c = num
    for n in range(0, num):
        if show:
            print(c, end=' ')
        c -= 1
        if c != 0:
            num = num * c
            if show:
                print('x', end=' ')
        else:
            if show:
                print('=', end=' ')
            break
    print(num)


fatorial(9)
