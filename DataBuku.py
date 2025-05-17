# 17 Mei 2025

print(f'\n{'DATA BUKU'.center(100,'=')}') 

listBuku = []

while True :
    print('\nMasukkan data buku')
    Judul = input('Judul buku : ').capitalize()
    Penulis = input('Penulis buku : ')

    Buku = [Judul,Penulis]
    listBuku.append(Buku)

    print(f'\n{'DATA BUKU'.center(40,'=')}')
    for index, item in enumerate(listBuku,start=1) :
        print(f'Buku ke-{index} : {item[0]} | {item[1]}')

    while True :
        lanjut = input('\nIngin menambah buku baru? (y/n) : ').lower()
        if lanjut in ['y','n'] : break
        else : print('Data yang anda masukkan tidak valid')
    
    if lanjut == 'n' : break
    
print('\nPROGRAM SELESAI\n')
print('DATA BUKU AKHIR'.center(40,'='))
for index, item in enumerate(listBuku,start=1) :
        print(f'Buku ke-{index} : {item[0]} | {item[1]}')
print('')
