def tambah(a, b):
    hasil = a + b
    return hasil


def kurang(a, b):
    hasil = a - b
    return hasil


def kali(a, b):
    hasil = a * b
    return hasil


def bagi(a, b):
    hasil = a / b
    return hasil


def mainmenu():
    opsi = "1. Penjumlahan \n2. Pengurangan \n3. Perkalian \n4. Pembagian\nX. Keluar"
    print(opsi)


while True:
    mainmenu()
    cal = input("Pilih opsi : ")

    if cal == 'X':
        print("Terima Kasih. Semoga harimu menyenangkan")
        break

    if cal not in ['1', '2', '3', '4']:
        print("Invalid Option")
        break
    while True:
        a = float(input("Masukkan angka pertama : "))
        b = float(input("Masukkan angka kedua : "))

        if cal == '1':
            print("Hasil = ", tambah(a, b))

        elif cal == '2':
            print("Hasil = ", kurang(a, b))

        elif cal == '3':
            print("Hasil = ", kali(a, b))

        elif cal == '4':
            print("Hasil = ", bagi(a, b))

        ulang = input("Anda ingin menghitung lagi? (Y/T) : ")
        if ulang == 'T':
            break
        elif ulang == 'Y':
            continue
