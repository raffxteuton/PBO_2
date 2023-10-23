# Fungsi untuk operasi penambahan
def tambah(x, y):
    return x + y

# Fungsi untuk operasi pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk operasi perkalian
def kali(x, y):
    return x * y

# Fungsi untuk operasi pembagian
def bagi(x, y):
    if y == 0:
        return "Pembagian oleh nol tidak diizinkan"
    return x / y

while True:
    print("Pilihan operasi:")
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '5':
        print("Keluar dari program.")
        break

    if pilihan not in ('1', '2', '3', '4'):
        print("Pilihan tidak valid. Silakan pilih kembali.")
        continue

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print("Hasil penambahan:", tambah(angka1, angka2))
    elif pilihan == '2':
        print("Hasil pengurangan:", kurang(angka1, angka2))
    elif pilihan == '3':
        print("Hasil perkalian:", kali(angka1, angka2))
    elif pilihan == '4':
        print("Hasil pembagian:", bagi(angka1, angka2))
