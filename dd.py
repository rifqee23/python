print("Kalkulator Duo")

while True:
    print("=" * 25)
    print('Operasi Matematika')
    print('  1. Jumlah \t [+]')
    print('  2. Kurang \t [-]')
    print('  3. Kali \t\t [*]')
    print('  4. Bagi \t\t [/]')
    print('  5. Keluar \t\t [x]')
    print("=" * 25)

    operasi = input('Pilih operasi (1/2/3/4/5): ')

    # Validasi input operasi
    if operasi not in ['1', '2', '3', '4', '5']:
        print('Operasi tidak valid, silakan masukkan angka 1-5')
        continue  # kembali ke awal loop

    if operasi == '5':
        print('Terima kasih telah menggunakan kalkulator kami')
        break  # keluar dari loop dan program

    if operasi == '1':
        print('User memilih penjumlahan')
    elif operasi == '2':
        print('User memilih pengurangan')
    elif operasi == '3':
        print('User memilih perkalian')
    elif operasi == '4':
        print('User memilih pembagian')

    # Input bilangan dan validasi
    while True:

            bilangan_1 = float(input('Masukkan bilangan pertama: '))
            bilangan_2 = float(input('Masukkan bilangan kedua: '))
            break  # keluar dari loop jika input valid

            print('Input tidak valid, silakan masukkan bilangan')

        if operasi == '1':
            hasil = bilangan_1 + bilangan_2
            print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
        elif operasi == '2':
            hasil = bilangan_1 - bilangan_2
            print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
        elif operasi == '3':
            hasil = bilangan_1 * bilangan_2
            print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
        elif operasi == '4':
            if bilangan_2 == 0:
                print('Tidak bisa membagi dengan nol')
            else:
                hasil = bilangan_1 / bilangan_2
                print(
                    f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')

    pilihan = input("Anda ingin menghitung lagi? (Y/T) : ")

    if pilihan == 'Y':
        continue
    elif pilihan == 'T':
        break
