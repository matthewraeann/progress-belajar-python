# 17 Mei 2025

listBuku = []
def tampilkan_buku(value) :
    print('\n'+'DATA BUKU TERBARU'.center(40,'=')+'\n')
    print(f'{'No.':<3}|{'Judul buku':<20}|{'Penulis buku':<20}')
    print('~'*40)
    for index, item in enumerate(value,start=1) :
        print(f'{index:<3}|{item.get('Judul buku'):<20}|{item.get('Penulis buku'):<20}')

print('\n'+'DATA BUKU'.center(100,'=')) 

while True :
    print('Masukkan data buku')
    Judul = input('Judul buku : ').title().strip()
    Penulis = input('Penulis buku : ').title().strip()

    Buku = {
         'Judul buku':Judul,
         'Penulis buku':Penulis
    }
    listBuku.append(Buku)

    tampilkan_buku(listBuku)

    while True :
        lanjut = input('\nIngin menambah buku baru? (y/n) : ').lower().strip()
        if lanjut in ['y','n'] :
            break
        else :
            print('Data yang anda masukkan tidak valid')
    
    if lanjut == 'n' : break
    
print('\nPROGRAM SELESAI')
tampilkan_buku(listBuku)