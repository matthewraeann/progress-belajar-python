# 18 Mei 2025

import os
import datetime
def tampilkan_data(value) :
    print('\n'+'DATA MAHASISWA TERBARU'.center(72)+'\n')
    print(f'{'Kode':<5}|{'Nama Mahasiswa':<35}|{'NPM':<10}|{'SKS':<4}|{'Tanggal Lahir':<12}')
    print(72*'~')
    for key in value : 
        nama = value[key]['Nama Mahasiswa']
        NPM = value[key]['NPM Mahasiswa']
        SKS = value[key]['SKS Lulus']
        lahir = value[key]['Tanggal Lahir'].strftime('%x')
        print(f'{key:<5}|{nama:<35}|{NPM:<10}|{SKS:<4}|{lahir:<12}')
data_invalid = '\nData yang anda masukkan tidak valid'

os.system('clear')

mahasiswa_template = {
    'Nama Mahasiswa':'nama',
    'NPM Mahasiswa':'NPM',
    'SKS Lulus':'SKS',
    'Tanggal Lahir':datetime.datetime(1111,1,22)
}
data_mahasiswa = {}

print('\n'+'DATA MAHASISWA'.center(72)+'\n')

while True :
    mahasiswa = dict.fromkeys(mahasiswa_template)
    while True : 
        mahasiswa['Nama Mahasiswa'] = input('Masukkan nama mahasiswa : ').title().strip()
        if all(kata.isalpha() for kata in mahasiswa['Nama Mahasiswa'].split()) == False :
            print(data_invalid)
        else :
            break
    while True : 
        try : 
            mahasiswa['NPM Mahasiswa'] = int(input('Masukkan NPM mahasiswa : '))
            break
        except :
            print(data_invalid)
    while True :
        try :
            mahasiswa['SKS Lulus'] = int(input('Masukkan SKS mahasiswa : '))
            break
        except :
            print(data_invalid)
    while True :
        while True :
            try :
                tanggal_lahir = int(input('Masukkan tanggal lahir mahasiswa (1-31): '))
            except :
                print(data_invalid)
                continue
            if tanggal_lahir not in range(1,32) :
                print(data_invalid)
            else :
                break
        while True :
            try :
                bulan_lahir = int(input('Masukkan bulan lahir mahasiswa (1-12) : '))
            except :
                print(data_invalid)
                continue
            if bulan_lahir not in range(1,13) :
                print(data_invalid)
            else :
                break
        while True :
            try :
                tahun_lahir = int(input('Masukkan tahun lahir mahasiswa (YYYY) : '))
            except :
                print(data_invalid)
                continue
            if tahun_lahir not in range(0,2026) :
                print(data_invalid)
            else :
                break
        try :
            mahasiswa['Tanggal Lahir'] = datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)
            break
        except : 
            print(data_invalid)

    i = len(data_mahasiswa)+1
    data_mahasiswa.update({f'MH{i:03}':mahasiswa})

    tampilkan_data(data_mahasiswa)
    while True :
        lanjut = input('Tambahkan Data Baru? (y/n) : ').lower().strip()
        if lanjut in ['y','n'] :
            break
        else :
            print(data_invalid)
    if lanjut == 'n' :
        break
print('\n'+'AKHIR DARI PROGRAM'.center(72,'='))
tampilkan_data(data_mahasiswa)
print('\n'+'TERIMA KASIH'.center(72)+'\n')