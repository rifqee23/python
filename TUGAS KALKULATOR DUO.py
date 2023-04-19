# fungsi untuk operasi penjumlahan
def tambah(a, b):
    return a + b

# fungsi untuk operasi pengurangan


def kurang(a, b):
    return a - b

# fungsi untuk operasi perkalian


def kali(a, b):
    return a * b

# fungsi untuk operasi pembagian


def bagi(a, b):
    return a / b

# fungsi untuk menampilkan menu


def menu():
    print("=== KALKULATOR DUO ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("X. Keluar")


while True:
    menu()
    op = input("Pilih opsi : ")

    if op == 'X':
        print("Terima Kasih. Sudah Menggunakan Kalkulator Duo")
        break

    if op not in ['1', '2', '3', '4']:
        print("PILIHAN INVALID")

    while True:
        a = float(input("Masukkan angka pertama : "))
        b = float(input("Masukkan angka kedua : "))

        if op == '1':
            print('User memilih penjumlan')
            print("Hasil = ", tambah(a, b))

        elif op == '2':
            print('User memilih pengurangan')
            print("Hasil = ", kurang(a, b))

        elif op == '3':
            print('User memilih perkalian')
            print("Hasil = ", kali(a, b))

        elif op == '4':
            print('User memilih pembagian')
            print("Hasil = ", bagi(a, b))

        ulang = input("Anda ingin menghitung lagi? (Y/T) : ")
        if ulang == 'T':
            break
        elif ulang == 'Y':
            continue
