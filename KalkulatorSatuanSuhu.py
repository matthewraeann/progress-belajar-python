# 17 Mei 2025

def is_number(value) :
    try : 
        float(value)
        return True
    except ValueError: 
        return False

while True :
    while True :
        print('Ketik "C" untuk Celcius\nKetik "R" untuk Reamur\nKetik "F" untuk Fahrenheit\nKetik "K" untuk Kelvin')
        satuan = input('Pilih satuan suhu yang ingin di konversi (C/R/F/K) : ').upper()
        if satuan == 'C' :
            while True :
                celcius = input('Masukkan suhu dalam celcius : ')
                if is_number(celcius) == True : 
                    celcius = float(celcius)
                    break
                else : print('\nHarap masukkan dalam bentuk angka')
            break
        elif satuan == 'R' :
            while True :
                reamur = input('Masukkan suhu dalam reamur : ')
                if is_number(reamur) == True : 
                    reamur = float(reamur)
                    celcius = 5/4*reamur
                    break
                else : print('\nHarap masukkan dalam bentuk angka')
            break
        elif satuan == 'F' :
            while True : 
                fahrenheit = input('Masukkan suhu dalam fahrenheit : ')
                if is_number(fahrenheit) == True : 
                    fahrenheit = float(fahrenheit)
                    celcius = (fahrenheit-32)*5/9
                    break
                else : print('\nHarap masukkan dalam bentuk angka')
            break
        elif satuan == 'K' :
            while True : 
                kelvin = input('Masukkan suhu dalam kelvin : ')
                if is_number(kelvin) == True : 
                    kelvin = float(kelvin)
                    celcius = kelvin-273
                    break
                else : print('\nHarap masukkan dalam bentuk angka')
            break
        else : 
            print('\nData yang anda masukkan tidak valid')

    reamur = 4/5*celcius 
    fahrenheit = 9/5*celcius + 32
    kelvin = celcius + 273

    def formating(value) :
        return f'{value:.2f}'.rstrip('0').rstrip('.')

    celcius = formating(celcius)
    reamur = formating(reamur)
    fahrenheit = formating(fahrenheit)
    kelvin = formating(kelvin)

    print(f'\nSuhu dalam celcius\t: {celcius}C')
    print(f'Suhu dalam reamur\t: {reamur}R')
    print(f'Suhu dalam fahrenheit\t: {fahrenheit}F')
    print(f'Suhu dalam kelvin\t: {kelvin}K\n')

    while True :
        start_over = input('Ingin mengkonversi data lain? (y/n) : ').lower()
        if start_over in ['y','n'] : break
        else : print('Data yang anda masukkan tidak valid')
    
    if start_over == 'n' : break
print(f'\n{'TERIMA KASIH'.center(50,'=')}\n')
