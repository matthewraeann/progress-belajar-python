# 18 Mei 2025

import os

os.system('cls')

def header(title = 'PROGRAM MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG') :
    print('\n'+title.center(80,'='))

def subheader(title) :
    print('\n'+title.center(50))

def input_nilai(jenis) :
    while True :
        try : 
            hasil = float(input(f'Masukkan nilai {jenis} : '))
            return hasil
        except ValueError :
            print('Data yang anda masukkan tidak valid\n')


def luas(panjang,lebar) :
    hasil = panjang * lebar
    return hasil

def keliling(panjang,lebar) :
    hasil = 2*(panjang+lebar)
    return hasil

def display(jenis,nilai) :
    nilai = f'{nilai:.2f}'.rstrip('0').rstrip('.')
    print(f'hasil perhitungan {jenis} = {nilai}')

def cek_lanjut() :
    while True :
        lanjut = input('\nBuat perhitungan baru? (y/n) : ').lower().strip()
        if lanjut not in ['y','n'] :
            print('Data yang anda masukkan tidak valid!')
        else :
            break
    if lanjut == 'n' :
        return False
    else :
        return True

header()
while True :
    subheader('MASUKKAN DATA')
    length = input_nilai('panjang')
    width = input_nilai('lebar')
    area = luas(length,width)
    circumference = keliling(length,width)
    subheader('HASIL')
    display('luas',area)
    display('keliling',circumference)
    if not cek_lanjut() :
        break
header('TERIMA KASIH')