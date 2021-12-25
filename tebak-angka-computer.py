import random

start = input(f'Pilihlah angka dari 1 sampai 1500, computer akan menebak angka yang kalian pikirkan, jika sudah siap ketik MULAI: ')

def tebakan_komputer(x):
    rendah = 1
    tinggi = x
    tanggapan = ''
    while tanggapan != 'c':
        if rendah != tinggi:
            tebakan = random.randint(rendah, tinggi)
        else:
            tebakan = rendah
        tanggapan = input(f'Apakah angka {tebakan} sudah benar. Jika terlalu tinggi(H), terlalu rendah(L), Jika benar(C): ')
        if tanggapan == 'h':
            tinggi = tebakan - 1
        elif tanggapan == 'l':
            rendah = tebakan + 1

    print(f'Wow! komputer dapat menebak angka {tebakan} kamu, dengan benar!!!')

if start == 'mulai':
    print(tebakan_komputer(1500))