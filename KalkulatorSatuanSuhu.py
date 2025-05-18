# 18 Mei 2025

import os
os.system('clear')
os.system('cls')

def header(title) :
    print(f'\n{title.center(56,'=')}\n')

def convert_to_celcius(jenis,nilai) :
    if jenis == 'R' :
        celcius = nilai*5/4
    elif jenis == 'F' :
        celcius = (nilai-32)*5/9
    elif jenis == 'K' :
        celcius = nilai-273
    else :
        celcius = nilai
    return celcius

def input_suhu(jenis) :
    while True :
        try : 
            nilai = float(input(f'\nMasukkan suhu dalam {jenis} : '))
            celcius = convert_to_celcius(jenis,nilai)
            return celcius
        except ValueError :
            print('\nHarap masukkan dalam bentuk angka')

def formating(value) :
        return f'{value:.2f}'.rstrip('0').rstrip('.')

def display(satuan,nilai,lambang) :
    print(f'Suhu dalam {satuan:<10} : {formating(nilai)}{lambang}')

def check_continue() :
    while True :
        start_over = input('\nIngin mengkonversi data lain? (y/n) : ').lower().strip()
        if start_over in ['y','n'] :
            return start_over == 'y'
        else:
            print('\nData yang anda masukkan tidak valid!')

header('KALKULATOR SUHU')

while True :
    while True :
        print('Ketik "C" untuk Celcius\nKetik "R" untuk Reamur\nKetik "F" untuk Fahrenheit\nKetik "K" untuk Kelvin')
        satuan = input('Pilih satuan suhu yang ingin di konversi (C/R/F/K) : ').upper().strip()
        if satuan in ['C','R','F','K'] :
            celcius = input_suhu(satuan)
            break
        else : 
            print('\nData yang anda masukkan tidak valid!')

    reamur = 4/5*celcius 
    fahrenheit = 9/5*celcius + 32
    kelvin = celcius + 273

    print('\nHASIL KONVERSI')
    display('celcius',celcius,'C')
    display('reamur',reamur,'R')
    display('fahrenheit',fahrenheit,'F')
    display('kelvin',kelvin,'K')

    if not check_continue() :
        break

header('TERIMA KASIH')