import random

def tebak(x):
    angka_acak = random.randint(1, x)
    tebak = 0
    while tebak != angka_acak:
        tebak = int(input(f'Tebak angka antara 1 sampai {x}: '))
        if tebak < angka_acak:
            print('Maaf, coba tebak lagi, terlalu rendah.')
        elif tebak > angka_acak:
            print('Maaf, coba tebak lagi, terlalu tinggi.')

    print(f'Wow, selamat. angka {angka_acak} adalah tebakan tepat!')

tebak(1500)