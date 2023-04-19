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

# fungsi utama


def main():
    pilihan = ''
    while pilihan != 'X':
        menu()
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            a = int(input("Masukkan bilangan pertama: "))
            b = int(input("Masukkan bilangan kedua: "))
            hasil = tambah(a, b)
            print("Hasil: ", hasil)

        elif pilihan == '2':
            a = int(input("Masukkan bilangan pertama: "))
            b = int(input("Masukkan bilangan kedua: "))
            hasil = kurang(a, b)
            print("Hasil: ", hasil)

        elif pilihan == '3':
            a = int(input("Masukkan bilangan pertama: "))
            b = int(input("Masukkan bilangan kedua: "))
            hasil = kali(a, b)
            print("Hasil: ", hasil)

        elif pilihan == '4':
            a = int(input("Masukkan bilangan pertama: "))
            b = int(input("Masukkan bilangan kedua: "))
            hasil = bagi(a, b)
            print("Hasil: ", hasil)

        elif pilihan == 'X':
            print("Terima kasih telah menggunakan Kalkulator Duo!")

        else:
            print("Pilihan tidak valid, silahkan coba lagi!")
            continue

        ulang = input("Anda ingin menghitung lagi? (Y/T) : ")
        if ulang == 'T':
            break
        elif ulang == 'Y':
            continue


# memanggil fungsi utama
main()
