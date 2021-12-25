import random

start = input(f'Di permainan ini kalian harus menebak angka yang di pikirkan oleh computer, jika sudah siap ketik MULAI: ')

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

if start == 'mulai':
    print (tebak(1500))