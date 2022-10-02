from time import sleep


def maior(* num):
    mai = 0
    for n in num:
        print(n, end=' ')
        sleep(0.3)
        if n > mai:
            mai = n
    print(f'Foram {len(num)} números ao todo.')
    print(f'O maior número foi {mai}')


maior(1)
